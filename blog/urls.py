from django.urls import path
from . import views
from .views import PostList

urlpatterns = [
    path('blog/', PostList.as_view(), name='blog'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]