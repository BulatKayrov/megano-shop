from rest_framework import serializers
from .models import Order
from product.serializers import ProductSerializers


class OrderSerializer(serializers.ModelSerializer):
    """
    Список заказов
    """
    products = ProductSerializers(many=True, required=True)

    class Meta:
        model = Order
        fields = '__all__'

