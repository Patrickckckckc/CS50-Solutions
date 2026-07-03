from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entry/<str:title>", views.entry, name="entry"),
    path("add/", views.add, name="add"),
    path("random/", views.random_page, name="random"),
    path("edit/<str:title>", views.edit_page, name="edit")
]
