from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'sku', 'display_categories']
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ['categories', 'name', 'price', 'sku']
    ordering = ['name']
    search_fields = ['name', 'price', 'sku', 'categories__name']

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    display_categories.short_description = 'Categories'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ("name",)}
