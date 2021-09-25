from django.shortcuts import render, get_object_or_404

from apps.category.models import Category
from .models import Product


def store(request, category_slug=None):
    products = Product.objects.all().filter(is_available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = dict(products=products)

    return render(request, 'store/store.html', context=context)


def product_detail(request, category_slug, product_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, category=category, slug=product_slug)

    context = dict(product=product)
    return render(request, 'store/product_detail.html', context=context)
