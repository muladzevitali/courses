from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import (render, get_object_or_404, redirect)

from apps.cart.models import (CartItem, get_cart_id)
from apps.category.models import Category
from apps.order.models import OrderProduct
from . import forms
from .models import (Product, ReviewRating, ProductGallery)


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
    is_purchased = OrderProduct.objects.filter(user_id=request.user.id, product=product).exists()
    reviews = ReviewRating.objects.filter(product=product, is_active=True)[:5]
    product_gallery = ProductGallery.objects.filter(product=product)
    context = dict(product=product, in_cart=in_cart, is_purchased=is_purchased, reviews=reviews,
                   average_rating=product.average_rating, reviews_count=product.reviews_count,
                   product_gallery=product_gallery)
    return render(request, 'store/product_detail.html', context=context)


@login_required()
def submit_review(request, product_id: int):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if not form.is_valid():
            messages.success(request, "Invalid parameters")

            return redirect(request.META.get('HTTP_REFERER'))

        product = get_object_or_404(Product, pk=product_id)

        try:
            review = ReviewRating.objects.get(user=request.user, product=product)
        except ReviewRating.DoesNotExist:
            review = ReviewRating(user=request.user, product=product)

        review.subject = form.cleaned_data['subject']
        review.review = form.cleaned_data['review']
        review.rating = form.cleaned_data['rating']
        review.ip = request.META.get('REMOTE_ADDR')
        review.save()

        messages.success(request, "Thank you! Your review has been submitted")
        return redirect(request.META.get('HTTP_REFERER'))
