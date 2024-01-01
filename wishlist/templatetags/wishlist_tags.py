from django import template
from wishlist.models import Wishlist

register = template.Library()


@register.filter(name='is_in_wishlist')
def is_in_wishlist(product, user):
    return Wishlist.objects.filter(user=user, product=product)
