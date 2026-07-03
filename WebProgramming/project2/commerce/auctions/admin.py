from django.contrib import admin
from .models import Listing, User

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "category", "user", "created_at")
    search_fields = ("title", "description")
    list_filter = ("category", "created_at")

admin.site.register(User)
