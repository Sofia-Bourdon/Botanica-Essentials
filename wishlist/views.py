from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_wishlist(request):
    """ A view that renders the wishlist page """
    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):
    """ Add a product to the wishlist """

    product = get_object_or_404(Product, pk=item_id)
    wishlist = request.session.get('wishlist', {})

    if item_id not in wishlist:
        wishlist[item_id] = True
        request.session['wishlist'] = wishlist
        messages.success(request, f'Added {product.name} to your wishlist!')
    else:
        messages.info(request, f'{product.name} is already in your wishlist!')

    return redirect(reverse('view_wishlist'))


def remove_from_wishlist(request, item_id):
    """ Remove a product from the wishlist """

    product = get_object_or_404(Product, pk=item_id)
    wishlist = request.session.get('wishlist', {})

    if item_id in wishlist:
        del wishlist[item_id]
        request.session['wishlist'] = wishlist
        messages.success(
            request, f'Removed {product.name} from your wishlist!')
    else:
        messages.error(
            request, f'Error removing {product.name} from your wishlist')

    return redirect(reverse('view_wishlist'))
