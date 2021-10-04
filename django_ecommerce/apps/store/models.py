from django.db import models
from django.urls import reverse
from django.db.models.aggregates import (Avg, Count)


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.FloatField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey('category.Category', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        aggregation = ReviewRating.objects.filter(product=self, is_active=True).aggregate(average=Avg('rating'))
        average = aggregation.get('average', 0)

        return average

    @property
    def reviews_count(self):
        aggregation = ReviewRating.objects.filter(product=self, is_active=True).aggregate(count=Count('rating'))
        count = aggregation.get('count', 0)

        return count

    @property
    def url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    @property
    def add_to_cart_url(self):
        return reverse('add_to_cart', args=[self.id])

    @property
    def remove_from_cart_url(self):
        return reverse('remove_from_cart', args=[self.id])

    @property
    def remove_cart_item_url(self):
        return reverse('remove_cart_item', args=[self.id])


class VariationManager(models.Manager):
    def colors(self):
        return super().filter(category='color', is_active=True)

    def sizes(self):
        return super().filter(category='size', is_active=True)


class Variation(models.Model):
    category_choices = (
        ('color', 'Color'),
        ('size', 'Size'),
    )
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=category_choices)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = VariationManager()

    def __str__(self):
        return f'{self.product} - {self.category} - {self.name}'


class ReviewRating(models.Model):
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subject}'
