from django.contrib import admin
from .models import Order, OrderProduct


class ProductOrder(admin.TabularInline):
    model = OrderProduct
    extra = 1
    fieldsets = (
        (None, {
            'fields': (('product', 'count'),)
        }),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ('address', 'customer')
    list_display = ('customer', 'city', 'address', 'total_cost', 'deliveryType', 'paymentType', 'createdAt')
    inlines = [ProductOrder]
    list_filter = ['paymentType', 'createdAt']
