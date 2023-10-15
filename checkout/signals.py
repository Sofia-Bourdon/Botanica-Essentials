from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import OrderLineItem, UserPurchase

# Your existing signals...


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()


@receiver(post_save, sender=User)
def create_user_purchase(sender, instance, created, **kwargs):
    """Post save signal to create UserPurchase record for new users."""
    if created:
        UserPurchase.objects.create(user=instance)
