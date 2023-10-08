from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'sku', 'category']
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ['category', 'name',
                   'price', 'sku']
    ordering = ['name']
    search_fields = ['name', 'price', 'sku', 'category__name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ("name",)}
