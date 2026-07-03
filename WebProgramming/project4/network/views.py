from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import math

from .models import User, Post, Reaction


def index(request):
    # Access all posts ordered by newest first
    posts = Post.objects.all().order_by('-timestamp')

    # Attach user_reaction to each post
    if request.user.is_authenticated:
        for post in posts:
            try:
                reaction = Reaction.objects.get(user=request.user, post=post)
                post.user_reaction = reaction.value  # "like" or "dislike"
            except Reaction.DoesNotExist:
                post.user_reaction = None
    else:
        for post in posts:
            post.user_reaction = None

    # Paginate: 10 posts per page
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "network/index.html", {
        "page_obj": page_obj
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def new_post(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            # Add a Django message (alert) and redirect
            return render(request, "network/index.html", {
                "message": "Requires login or register."
            })

        # Get content from POST form
        content = request.POST.get("new-post-content", "").strip()

        if content:
            post = Post.objects.create(user=request.user, content=content)
            # Redirect back to index after creating post
            return redirect("index")

        # If empty content, show error
        return redirect("index")

    # If not POST, return error
    return JsonResponse({"error": "POST request required."}, status=400)


@login_required
def profile_page(request, id):
    # Get User
    profile_user = get_object_or_404(User, pk=id)

    # Get Posts for this user
    posts = Post.objects.filter(user=profile_user).order_by('-timestamp')

    # Attach user_reaction for each post
    for post in posts:
        try:
            reaction = Reaction.objects.get(user=request.user, post=post)
            post.user_reaction = reaction.value  # "like" or "dislike"
        except Reaction.DoesNotExist:
            post.user_reaction = None

    # Create Paginator: 10 posts per page
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Render Template
    return render(request, "network/profile_page.html", {
        "profile_user": profile_user,
        "page_obj": page_obj
    })

@login_required
def follow_toggle(request, id):
    target_user = get_object_or_404(User, pk=id)

    # Prevent following yourself
    if request.user != target_user:
        if target_user in request.user.following.all():
            request.user.following.remove(target_user)
        else:
            request.user.following.add(target_user)

    return redirect("profile_page", id=id)

@login_required
def following_view(request):
    # Get posts from people the user follows
    posts = Post.objects.filter(user__in=request.user.following.all()).order_by("-timestamp")

    # Attach user_reaction to each post
    for post in posts:
        try:
            reaction = Reaction.objects.get(user=request.user, post=post)
            post.user_reaction = reaction.value  # "like" or "dislike"
        except Reaction.DoesNotExist:
            post.user_reaction = None

    # Paginate as usual
    from django.core.paginator import Paginator
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "network/following.html", {"page_obj": page_obj})

@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, pk=id, user=request.user)

    if request.method == "POST":
        new_content = request.POST.get("content")
        post.content = new_content
        post.save()

        # Always return JSON for fetch()
        return JsonResponse({
            "success": True,
            "content": post.content,
            "post_id": post.id
        })

    # Optional: handle GET requests
    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)

@login_required
def toggle_like(request, id):
    post = get_object_or_404(Post, pk=id)
    reaction, created = Reaction.objects.get_or_create(user=request.user, post=post)

    if reaction.value == "like":
        # Remove like
        reaction.delete()
        post.likes -= 1
        user_reaction = None
    else:
        # Switch from dislike if needed
        if reaction.value == "dislike":
            post.dislikes -= 1
        reaction.value = "like"
        reaction.save()
        post.likes += 1
        user_reaction = "like"

    post.save()
    return JsonResponse({"success": True, "likes": post.likes, "dislikes": post.dislikes, "user_reaction": user_reaction})


@login_required
def toggle_dislike(request, id):
    post = get_object_or_404(Post, pk=id)
    reaction, created = Reaction.objects.get_or_create(user=request.user, post=post)

    if reaction.value == "dislike":
        # Remove dislike
        reaction.delete()
        post.dislikes -= 1
        user_reaction = None
    else:
        # Switch from like if needed
        if reaction.value == "like":
            post.likes -= 1
        reaction.value = "dislike"
        reaction.save()
        post.dislikes += 1
        user_reaction = "dislike"

    post.save()
    return JsonResponse({"success": True, "likes": post.likes, "dislikes": post.dislikes, "user_reaction": user_reaction})

