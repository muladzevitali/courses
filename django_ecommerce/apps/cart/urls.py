from django.urls import path

from . import views

urlpatterns = [
    path('', views.cart_index, name='cart'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>', views.remove_from_cart, name='remove_from_cart'),
    path('remove_cart_item/<int:product_id>', views.remove_cart_item, name='remove_cart_item')
]
