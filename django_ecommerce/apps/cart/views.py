from django.shortcuts import (render, get_object_or_404, redirect)

from apps.store.models import (Product, Variation)
from .models import (Cart, CartItem, get_cart_id)


def cart_index(request):
    cart, _ = Cart.objects.get_or_create(cart_id=get_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)

    total = sum(cart_item.product.price * cart_item.quantity for cart_item in cart_items)
    quantity = sum(cart_item.quantity for cart_item in cart_items)
    tax = 0.02 * total
    grand_total = total + tax

    context = dict(cart=cart, cart_items=cart_items, total=total, quantity=quantity, tax=tax, grand_total=grand_total)

    return render(request, 'cart/cart.html', context=context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, stock__gt=0)

    product_variations = list()
    if request.method == "POST":
        for key, value in request.POST.items():
            try:
                variation = Variation.objects.get(product=product, category__iexact=key, name__iexact=value)
                product_variations.append(variation)
            except Variation.DoesNotExist:
                continue

    cart_id = get_cart_id(request)
    cart, _ = Cart.objects.get_or_create(cart_id=cart_id)

    cart_items = CartItem.objects.filter(product=product, cart=cart)

    if cart_items:
        for item in cart_items:
            existing_variations = item.variations.all()
            if list(existing_variations) == product_variations:
                item.quantity += 1
                item.save()

                return redirect('cart')

    cart_item = CartItem.objects.create(product=product, cart=cart, quantity=1)
    for variation in product_variations:
        cart_item.variations.add(variation)
    cart_item.save()

    return redirect('cart')


def remove_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)

    cart_item.delete()

    return redirect('cart')


def increment_cart_item_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')


def decrement_cart_item_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')
