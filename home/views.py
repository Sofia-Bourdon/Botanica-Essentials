from django.shortcuts import render
from products.models import Product, Category


def index(request):
    essentials_products = Product.objects.filter(categories__slug='essentials')
    context = {
        'products': essentials_products
    }
    return render(request, 'home/index.html', context)


def privacy_policy(request):
    return render(request, 'home/privacy_policy.html')


def faq(request):
    return render(request, 'home/faq.html')


def our_philosophy(request):
    return render(request, 'home/our_philosophy.html')

def custom_404(request, exception):
    """Display a custom 404 page"""
    return render(request, 'home/404.html', status=404)