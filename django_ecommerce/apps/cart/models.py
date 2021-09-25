from django.db import models
from django.urls import reverse


def get_cart_id(request):
    return request.session.session_key or request.session.create()


# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cart_id}'


class CartItem(models.Model):
    cart = models.ForeignKey('cart.Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    variations = models.ManyToManyField('store.Variation', blank=True)
    quantity = models.SmallIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.cart} - {self.product}'

    @property
    def increment_cart_item_quantity_url(self):
        return reverse('increment_cart_item_quantity', args=[self.id])

    @property
    def decrement_cart_item_quantity_url(self):
        return reverse('decrement_cart_item_quantity', args=[self.id])

    @property
    def remove_cart_item_url(self):
        return reverse('remove_cart_item', args=[self.id])

    @property
    def total(self):
        return self.product.price * self.quantity
