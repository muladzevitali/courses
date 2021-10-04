from django.urls import path
from . import views


urlpatterns = [
    path('place-order/', views.place_order, name='place_order'),
    path('post-payment/', views.post_payment, name='post_payment'),
    path('order-complete/', views.order_complete, name='order_complete'),
]
