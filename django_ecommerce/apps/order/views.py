import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from apps.cart.models import CartItem
from apps.cart.views import get_cart_info
from .forms import OrderForm
from .models import (Order, Payment, OrderProduct)


@login_required()
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    if not cart_items:
        return redirect('store')

    total = sum(cart_item.product.price * cart_item.quantity for cart_item in cart_items)
    tax = 0.02 * total

    form = OrderForm(request.POST)
    if request.method == 'POST':
        if not form.is_valid():
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

        context = dict(order=order, cart_items=cart_items, total=total, tax=tax, grand_total=tax + total)
        return render(request, 'order/place-order.html', context=context)

    context = dict(form=form)
    return render(request, 'order/place-order.html', context=context)


def post_payment(request):
    payment_data = json.loads(request.body)

    order = get_object_or_404(Order, user=request.user, is_ordered=False, order_number=payment_data['orderNumber'])

    payment = Payment(user=request.user,
                      payment_id=payment_data['transactionID'],
                      payment_method=payment_data['paymentMethod'],
                      amount_paid=order.order_total,
                      status=payment_data['status'])
    payment.save()
    order.payment = payment
    order.is_ordered = True
    order.status = payment_data['status'].capitalize()
    order.save()

    cart_items = CartItem.objects.filter(user=request.user)
    for cart_item in cart_items:
        order_product = OrderProduct(user=request.user, order=order, payment=payment, product=cart_item.product)

        order_product.quantity = cart_item.quantity
        order_product.product_price = cart_item.product.price
        order_product.is_ordered = True

        order_product.save()
        order_product.variations.set(cart_item.variations.all())

        order_product.save()

        product = cart_item.product
        product.stock -= cart_item.quantity
        product.save()

    cart_items.delete()

    subject = 'Thank you for your order'
    message = render_to_string('order/order-received-email.html', {
        'user': request.user.email,
        'order': order,
    })
    email = EmailMessage(subject, message, to=[request.user.email])
    email.send()

    data = dict(order_number=order.order_number, payment_id=payment.payment_id)

    return JsonResponse(data)


def order_complete(request):
    order_number = request.GET.get('order_number')
    payment_id = request.GET.get('payment_id')

    payment = get_object_or_404(Payment, payment_id=payment_id)
    order = get_object_or_404(Order, order_number=order_number, payment=payment, is_ordered=True)
    order_products = order.orderproduct_set.all()
    total = sum(order_product.product_price * order_product.quantity for order_product in order_products)
    tax = 0.02 * total
    grand_total = total + tax

    context = dict(order=order, order_products=order_products, payment=payment, total=total)

    return render(request, 'order/order-complete.html', context=context)
