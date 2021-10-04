from django.contrib import admin

from .models import (Product, Variation, ReviewRating)


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'category', 'modified_at', 'is_available']
    prepopulated_fields = {'slug': ('name',)}


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'category', 'name', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('product',)
    list_filter = ('product', 'category', 'name',)


class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'rating')


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
