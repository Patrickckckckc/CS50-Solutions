from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Users can follow other users
    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following",
        blank=True
    )

    def followers_count(self):
        return self.followers.count()

    def following_count(self):
        return self.following.count()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "posts")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}: {self.content[:30]}"

class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(max_length=10, choices=[("like", "Like"), ("dislike", "Dislike")])

    class Meta:
        unique_together = ("user", "post")  # one reaction per user per post
