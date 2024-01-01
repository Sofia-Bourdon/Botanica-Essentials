from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from user.models import UserProfile


class Wishlist(models.Model):
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user}'s wishlist item: {self.product}"
