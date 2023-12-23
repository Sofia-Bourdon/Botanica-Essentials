from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'blog/blog.html' 
    context_object_name = 'posts'
