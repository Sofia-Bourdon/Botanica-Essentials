from django.contrib import admin
from .models import Wishlist

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'timestamp', 'product']
    list_filter = ['user', 'timestamp', 'product']
    search_fields = ['user', 'timestamp', 'product']

