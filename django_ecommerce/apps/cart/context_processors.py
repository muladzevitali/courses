from .models import (CartItem, get_cart_id)


def cart_item_counter(request):
    if 'admin' in request.path:
        return dict()

    cart_items = CartItem.objects.filter(cart__cart_id=get_cart_id(request), is_active=True)
    num_items_in_cart = sum(cart_item.quantity for cart_item in cart_items)

    return dict(num_items_in_cart=num_items_in_cart)
