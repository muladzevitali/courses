from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (render, redirect)

from apps.cart.models import CartItem
from apps.cart.views import get_cart_info
from .forms import OrderForm
from .models import Order


@login_required()
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    if not cart_items:
        return redirect('store')

    total = sum(cart_item.product.price * cart_item.quantity for cart_item in cart_items)
    tax = 0.02 * total

    form = OrderForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            messages.error(request, 'Incorrect values')

            cart_info = get_cart_info(request)
            context = dict(form=form, **cart_info)
            return render(request, 'cart/checkout.html', context=context)

        order = Order(user=request.user)
        order.first_name = form.cleaned_data['first_name']
        order.last_name = form.cleaned_data['last_name']
        order.email = form.cleaned_data['email']
        order.phone = form.cleaned_data['phone']
        order.address_line_1 = form.cleaned_data['address_line_1']
        order.address_line_2 = form.cleaned_data['address_line_2']
        order.city = form.cleaned_data['city']
        order.state = form.cleaned_data['state']
        order.country = form.cleaned_data['country']
        order.order_note = form.cleaned_data['order_note']
        order.order_total = total + tax
        order.tax = tax
        order.ip = request.META.get('REMOTE_ADDR')
        order.save()

        return redirect('checkout')

    context = dict(form=form)
    return render(request, 'order/place-order.html', context=context)


def payment(request):

    return render(request, 'order/place-order.html')