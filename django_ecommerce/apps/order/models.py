from datetime import datetime

from django.db import models
from django.db.models.signals import post_save


class Payment(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=20)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.payment_id}'


class Order(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled')
    )

    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey('order.Payment', on_delete=models.SET_NULL, null=True, blank=True)
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    order_note = models.CharField(max_length=999)
    order_total = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='New')
    ip = models.CharField(max_length=20, blank=True)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'

    def __str__(self):
        return f'{self.order_number} - {self.user}'

    @staticmethod
    def create_order_id(sender, instance: 'Order', **kwargs):
        if instance.order_number:
            return

        current_date = datetime.now().strftime('%Y%m%d')
        instance.order_number = f'{current_date}{instance.id}'
        instance.save()


class OrderProduct(models.Model):
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    payment = models.ForeignKey('order.Payment', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    variations = models.ManyToManyField('store.Variation', blank=True)
    quantity = models.SmallIntegerField()
    product_price = models.FloatField()
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def order_product_total(self):
        return self.quantity * self.product_price

    def __str__(self):
        return f'{self.order} - {self.user}'


post_save.connect(Order.create_order_id, sender=Order)
