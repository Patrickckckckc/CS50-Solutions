from django.test import TestCase, Client
from django.urls import reverse
from .models import Post, User

# Create your tests here.
# Show Posts
class PostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="patrick", password="12345")
        self.post = Post.objects.create(user=self.user, content= "Hello world")

    def test_index_page_loads(self):
        c = Client()
        c.login(username="patrick", password="12345")
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello world")

    def test_no_posts_yet(self):
        Post.objects.all().delete()
        c = Client()
        c.login(username="patrick", password="12345")
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts yet — be the first to share!")

    def test_posts_ordered(self):
        older_post = Post.objects.create(user=self.user, content="Older post")
        newer_post = Post.objects.create(user=self.user, content="Newer post")

        c = Client()
        c.login(username="patrick", password="12345")
        response = c.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Older post")
        self.assertContains(response, "Newer post")

        # Check ordering
        content = response.content.decode()
        self.assertLess(content.index("Newer post"), content.index("Older post"))


# Create NewPosts
class NewPostTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="patrick", password="12345")
        self.client = Client()

    def test_new_post_requires_login(self):
        # Try posting without logging in
        response = self.client.post("/new_post", {"new-post-content": "Hello world"})
        self.assertEqual(response.status_code, 200)  # Redirect or render
        self.assertContains(response, "Requires login or register.")

    def test_new_post_success(self):
        # Log in first
        self.client.login(username="patrick", password="12345")
        response = self.client.post("/new_post", {"new-post-content": "Hello world"})
        # After redirect, check that post exists
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.content, "Hello world")
        self.assertEqual(post.user.username, "patrick")

    def test_new_post_empty_content(self):
        self.client.login(username="patrick", password="12345")
        response = self.client.post("/new_post", {"new-post-content": ""})
        # Should not create a post
        self.assertEqual(Post.objects.count(), 0)

# Follow / Unfollow
class FollowTests(TestCase):

    def setUp(self):
        # Create two users
        self.alice = User.objects.create_user(username="alice", password="12345")
        self.bob = User.objects.create_user(username="bob", password="12345")

        # Log in Alice
        self.client = Client()
        self.client.login(username="alice", password="12345")

    def test_follow_user(self):
        # Alice follows Bob
        response = self.client.post(reverse("follow_toggle", args=[self.bob.id]))
        self.assertEqual(response.status_code, 302)  # redirect back to profile

        # Bob should now have Alice as a follower
        self.assertIn(self.alice, self.bob.followers.all())
        self.assertIn(self.bob, self.alice.following.all())

    def test_unfollow_user(self):
        # First, Alice follows Bob
        self.client.post(reverse("follow_toggle", args=[self.bob.id]))
        # Then, Alice unfollows Bob
        response = self.client.post(reverse("follow_toggle", args=[self.bob.id]))
        self.assertEqual(response.status_code, 302)

        # Bob should no longer have Alice as a follower
        self.assertNotIn(self.alice, self.bob.followers.all())
        self.assertNotIn(self.bob, self.alice.following.all())

    def test_cannot_follow_self(self):
        # Alice tries to follow herself
        response = self.client.post(reverse("follow_toggle", args=[self.alice.id]))
        self.assertEqual(response.status_code, 302)

        # Alice should not appear in her own followers/following
        self.assertNotIn(self.alice, self.alice.followers.all())
        self.assertNotIn(self.alice, self.alice.following.all())
