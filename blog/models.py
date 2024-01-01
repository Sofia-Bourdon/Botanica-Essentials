from django.db import models
from django.contrib.auth.models import User
import cloudinary


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = cloudinary.models.CloudinaryField('image', null=True, blank=True)
