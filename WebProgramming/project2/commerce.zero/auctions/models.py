from django.contrib.auth.models import AbstractUser
from django.db import models

# User Model
class User(AbstractUser):
    pass

# Listings Model
class Listing(models.Model):
    CATEGORY_CHOICES = [
        ("ELEC", "Electronics"),
        ("FASH", "Fashion"),
        ("HOME", "Home & Garden"),
        ("TOYS", "Toys & Games"),
        ("BOOK", "Books"),
        ("SPORT", "Sports"),
        ("AUTO", "Automotive"),
        ("MUSIC", "Music"),
        ("MOVIE", "Movies"),
        ("OTHER", "Other"),
    ]
    title = models.CharField(max_length=30)
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField(default="NO DESCRIPTION")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="OTHER")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


# Bids Model
class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Comments Model
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Watchlist Model
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        # Prevent duplicates: one user can't watch the same listing twice
        unique_together = ("user", "listing")

        # Default ordering: newest first
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} → {self.listing.title}"
