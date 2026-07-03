from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from decimal import Decimal, InvalidOperation


from .models import User, Listing, Watchlist, Bid, Comment


def index(request):
    # Access to all the Listing
    listings = Listing.objects.all().order_by("-created_at")
    if request.user.is_authenticated:
        user_watchlist_ids = Watchlist.objects.filter(user=request.user).values_list("listing_id", flat=True)
    else:
        user_watchlist_ids = []

    return render(request, "auctions/index.html", {
        "listings" : listings,
        "user_watchlist_ids": list(user_watchlist_ids)
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

# ADD A NEW LISTING
@login_required
def addlisting(request):
    # POST -> Submit the form succesfully
    if request.method == "POST":
        # Get Title
        title = request.POST.get("title")
        description = request.POST.get("description")
        price = request.POST.get("price")
        image_url = request.POST.get("image_url")
        category = request.POST.get("category")

        # Check Valid Input
        if not title or not description or not price:
            return render(request, "auctions/index.html", {
                "message": "MISSING INFORMATION"
            })

        # Check Correct Price
        try:
            price = Decimal(price)
        except (ValueError, InvalidOperation):
            return render(request, "auctions/index.html", {
            "message": "INVALID PRICE FORMAT"
            })

        if price <= 0:
            return render(request, "auctions/index.html", {
            "message": "INVALID PRICE"
            })

        # Add the correspond value
        listing = Listing(
            title=title,
            description=description,
            price=price,
            image_url=image_url,
            category=category if category else "OTHER",
            user=request.user
        )
        listing.save()

        return redirect("index")

    # GET -> Render the form page
    else:
        return render(request, "auctions/add_listing.html")


# CANCEL LISTING
@login_required
def cancel_listing(request, id):
    listing = get_object_or_404(Listing, pk=id)
    if listing.user != request.user:
        return redirect("error", message="You are not allowed to cancel this listing")
    listing.is_active = False
    listing.save()
    return redirect(reverse("listing", args=[listing.id]))


# SHOW ALL THE INFORMATION OF A SINGLE LISTING
def listing(request, id):
    listing = get_object_or_404(Listing, pk=id)

    user_bid = None
    user_watchlist_ids = []
    cancel_auction_option = False
    winner_auction_option = False

    if request.user.is_authenticated:
        user_bid = Bid.objects.filter(user=request.user, listing=listing).order_by("-timestamp").first()
        user_watchlist_ids = Watchlist.objects.filter(user=request.user).values_list("listing_id", flat=True)
        cancel_auction_option = listing.user == request.user

        if user_bid and user_bid.amount == listing.price:
            winner_auction_option = True

    comments = Comment.objects.filter(listing=listing).order_by("-created_at")

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "user_watchlist_ids": user_watchlist_ids,
        "comments": comments,
        "cancel_auction_option": cancel_auction_option,
        "winner_auction_option": winner_auction_option
    })


# SHOW ALL LISTINGS OF AN SPECIFY CATEGORY
def category(request, category):
    listings = Listing.objects.filter(category=category).order_by("-created_at")

    return render(request, "auctions/category.html", {
        "category": category,
        "listings": listings
    })

# SHOW ALL POSIBLE CATEGORIES
def categories(request):
    return render(request, "auctions/categories.html")

# WATCH LIST
# Add / Delete Watchlist
@login_required
def toggle_watchlist(request, id):
    if request.method == "POST":
        listing =  get_object_or_404(Listing, id=id)
        watchlist_item, created = Watchlist.objects.get_or_create(
            user=request.user,
            listing=listing
        )

        if not created:
            watchlist_item.delete()

        return redirect(request.META.get("HTTP_REFERER", "index"))



# Take as parameter the listings on the Watchlist
@login_required
def watchlist(request):
    # Get all the items on my watchlist
    watchlist_items = Watchlist.objects.filter(user=request.user)
    listings = [item.listing for item in watchlist_items]

    return render(request, "auctions/watchlist.html", {
        "listings" : listings
    })

# ADD BID
@login_required
def add_bid(request, id):
    if request.method == "POST":
        # Get INPUT
        listing = get_object_or_404(Listing, pk=id)
        try:
            bid_amount = Decimal(request.POST.get("bid"))
        except(ValueError, InvalidOperation):
            return redirect(reverse("error", kwargs={"message": "Invalid amount"}))


        # Check if the bid is correct -> Print a message in case is Wrong / Delete Bid
        if bid_amount > listing.price:
            # Create Bid
            Bid.objects.create(
            amount=bid_amount,
            listing=listing,
            user=request.user
            )

            # Correct Current Price in Listing
            listing.price = bid_amount
            listing.save()

            # Redirect into the same page
            return redirect(request.META.get("HTTP_REFERER", "index"))

        else:
            return redirect(reverse("error", kwargs={"message": "Your bid must be greater than the current price"}))


# COMMENT SECTIONS
@login_required
def add_comment(request, id):
    if request.method == "POST":
        listing = get_object_or_404(Listing, id=id)
        content = request.POST.get("content")

        if content.strip():
            Comment.objects.create(
                content=content,
                listing=listing,
                user=request.user
            )

        # Redirect into the same page
        return redirect(request.META.get("HTTP_REFERER", "index"))

# Error
def error(request, message):
    return render(request, "auctions/error.html", {
        "message": message
    })



