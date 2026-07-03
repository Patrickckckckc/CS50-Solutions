from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("addlisting", views.addlisting, name="addlisting"),
    path("listing/<int:id>/", views.listing, name="listing"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>/", views.category, name="category"),
    path("watchlist/toggle/<int:id>/", views.toggle_watchlist, name="toggle_watchlist"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("listing/<int:id>/comment/", views.add_comment, name="add_comment"),
    path("listing/<int:id>/add_bid", views.add_bid, name="add_bid"),
    path("error/<str:message>/", views.error, name="error"),
    path("cancel_listing/<int:id>/", views.cancel_listing, name="cancel_listing")
]
