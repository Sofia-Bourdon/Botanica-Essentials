from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    # Define redirect_url at the start
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if quantity <= 0:
        messages.error(
            request,
            "Invalid quantity! Please enter a number greater than 0.")
        return redirect(redirect_url)  # redirect_url is now always defined

    if item_id in bag:
        bag[item_id] += quantity
        messages.success(
            request,
            f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Added {product.name} to your bag successfully')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id, None)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def delete_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    if item_id in bag:
        del bag[item_id]
        request.session['bag'] = bag
        messages.success(request, f'Removed {product.name} from your bag')
    else:
        messages.error(request, f'Error removing item: {item_id}')

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))
