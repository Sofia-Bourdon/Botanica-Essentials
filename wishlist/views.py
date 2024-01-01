from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.models import UserProfile
from .models import Wishlist

from products.models import Product


@login_required
def view_wishlist(request):
    """ A view that renders the wishlist page """

    if not request.user.is_authenticated:
        messages.info(
            request,
            'You need to be logged in to view your wishlist.')
        return redirect(reverse('account_login'))

    user_profile = request.user.userprofile
    wishlist_items = Wishlist.objects.filter(user=user_profile)
    context = {
        'wishlist_items': wishlist_items
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, item_id):
    """ Add a product to the wishlist """

    if not request.user.is_authenticated:
        messages.info(
            request,
            'You need to be logged in to add items to your wishlist.')
        return redirect(reverse('account_login'))

    product = get_object_or_404(Product, pk=item_id)
    user_profile = request.user.userprofile

    # Check if the product is already in the wishlist
    if Wishlist.objects.filter(user=user_profile, product=product).exists():
        messages.info(request, f'{product.name} is already in your wishlist!')
    else:
        Wishlist.objects.create(user=user_profile, product=product)
        messages.success(request, f'Added {product.name} to your wishlist!')

    return redirect(reverse('view_wishlist'))


def remove_from_wishlist(request, item_id):
    if not request.user.is_authenticated:
        messages.info(
            request,
            'You need to be logged in to remove items from your wishlist.')
        return redirect(reverse('account_login'))

    product = get_object_or_404(Product, pk=item_id)
    user_profile = request.user.userprofile
    wishlist_item = Wishlist.objects.filter(user=user_profile, product=product)

    if wishlist_item.exists():
        wishlist_item.delete()
        messages.success(
            request,
            f'Removed {product.name} from your wishlist!')
    else:
        messages.error(
            request,
            f'Error removing {product.name} from your wishlist')

    return redirect(reverse('view_wishlist'))
