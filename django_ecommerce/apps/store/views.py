from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from apps.cart.models import (CartItem, get_cart_id)
from apps.category.models import Category
from .models import Product


def store(request, category_slug=None):
    products = Product.objects.all().filter(is_available=True).order_by('-created_at')
    if request.GET.get('keyword'):
        keyword = request.GET.get('keyword')
        products = products.filter(Q(name__iregex=keyword) | Q(description__iregex=keyword))

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, per_page=6)
    page = request.GET.get('page')

    context = dict(products=paginator.get_page(page))

    return render(request, 'store/store.html', context=context)


def product_detail(request, category_slug, product_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, category=category, slug=product_slug)

    in_cart = CartItem.objects.filter(cart__cart_id=get_cart_id(request), product=product).exists()

    context = dict(product=product, in_cart=in_cart)
    return render(request, 'store/product_detail.html', context=context)

