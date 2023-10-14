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