from django.contrib import admin

from .models import (Payment, Order, OrderProduct)


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'full_name', 'email', 'phone', 'order_total', 'tax', 'status', 'ip')
    list_filter = ('status', 'is_ordered',)
    search_fields = ('order_number', 'first_name', 'last_name', 'email', 'phone')
    list_per_page = 50
    inlines = (OrderProductInline,)


admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
