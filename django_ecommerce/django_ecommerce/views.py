from django.shortcuts import render

from apps.store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('-created_at')

    context = dict(products=products)
    return render(request, 'index.html', context=context)
