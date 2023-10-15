from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from products.models import Product
from .models import Order, UserPurchase
from .forms import OrderForm
from decimal import Decimal


def get_order_total_and_discount(bag, user):
    order_total = Decimal('0')  # Use decimal directly

    for product_id, quantity in bag.items():
        product = Product.objects.get(id=product_id)
        lineitem_total = product.price * Decimal(str(quantity))
        order_total += lineitem_total

    discount = Decimal('0')
    user_purchase, _ = UserPurchase.objects.get_or_create(user=user)
    if not user_purchase.has_made_purchase:
        # Convert the float to a Decimal here
        discount = order_total * Decimal('0.10')

    return order_total, discount


def handle_post_request(request, order_total, discount):
    order_form = OrderForm(request.POST)
    if order_form.is_valid():
        order = order_form.save(commit=False)
        order.user = request.user
        order.discount = discount
        order.order_total = order_total
        order.grand_total = order_total - discount
        order.save()

        user_purchase = UserPurchase.objects.get(user=request.user)
        user_purchase.has_made_purchase = True
        user_purchase.save()

        messages.success(request, "Your order has been successfully placed!")
        return redirect(reverse('products'))

    return None


def checkout(request):
    if not request.user.is_authenticated:
        messages.error(
            request, "Please log in or sign up to proceed with checkout.")
        return redirect(reverse('login'))

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_total, discount = get_order_total_and_discount(bag, request.user)

    if request.method == "POST":
        response = handle_post_request(request, order_total, discount)
        if response:
            return response

    order_form = OrderForm()
    grand_total = order_total - discount
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'order_total': order_total,
        'grand_total': grand_total,
        'discount': discount
    }

    return render(request, template, context)
