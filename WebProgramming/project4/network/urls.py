
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("profile_page/<int:id>/", views.profile_page, name="profile_page"),
    path("follow_toggle/<int:id>/", views.follow_toggle, name="follow_toggle"),
    path("following/", views.following_view, name="following"),
    path("edit/<int:id>/", views.edit_post, name="edit_post"),
    path("toggle_like/<int:id>/", views.toggle_like, name="toggle_like"),
    path("toggle_dislike/<int:id>/", views.toggle_dislike, name="toggle_dislike"),
]
