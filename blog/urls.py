from django.urls import path
from . import views
from .views import BlogList

urlpatterns = [
    path('', BlogList.as_view(), name='blog'),
    path('<post_id>/', views.blog_detail, name='blog_detail'),
    path('delete/<int:post_id>/', views.delete_blog, name='delete_blog'),
]