from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Post

class BlogList(ListView):
    """ A view to show a list of all the blog posts"""
    model = Post
    template_name = 'blog/blog.html' 
    context_object_name = 'posts'


def blog_detail(request, post_id):
    """ A view to show individual post details """

    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def delete_blog(request, post_id):
    """ Delete a blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted sucessfully!')
    return redirect(reverse('blog'))

