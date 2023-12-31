from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'timestamp')
    search_fields = ['author', 'title', 'body']
    list_filter = ('author', 'title')
