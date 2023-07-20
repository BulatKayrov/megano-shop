from django.contrib.auth.models import User
from django.db import models
from product.models import Products
from profile_app.models import Profile


class Order(models.Model):
    """Модель заказа"""
    delivery_choices = (
        ('free', 'Free'),
        ('paid', 'Paid'),
    )
    payment_choices = (
        ('online', 'Online'),
        ('cash', 'Cash'),
    )
    status_choices = (
        ('accepted', 'Accepted'),
        ('processing', 'Processing'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed')
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')
    deliveryType = models.CharField(choices=delivery_choices, max_length=200)
    paymentType = models.CharField(choices=payment_choices, max_length=200)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(choices=status_choices, max_length=200)
    city = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    products = models.ManyToManyField(Products, related_name='orders', verbose_name='продуты')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.address


class OrderProduct(models.Model):
    """Модель продуктов заказа"""
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name='Адрес доставки', related_name='order_products'
    )

    class Meta:
        verbose_name = 'Продукт в заказе'
        verbose_name_plural = 'Продукты в заказе'

    def __str__(self):
        return str(self.product.title)
