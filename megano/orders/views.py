from typing import Any
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from product.models import Products
from .models import Order, OrderProduct
from .serializers import OrderSerializer


class OrderListApiView(APIView):

    """История заказов и оформление заказа"""

    def get(self, request: Request) -> Response:
        """Отображение истории заказов"""
        data = Order.objects.filter(customer__user__username=request.user)
        serialized = OrderSerializer(data, many=True)
        return Response(serialized.data)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Создание заказа"""
        products_in_order = [(obj["id"], obj["count"], obj["price"]) for obj in request.data]
        products = Products.objects.filter(id__in=[obj[0] for obj in products_in_order])
        order = Order.objects.create(
            customer=request.user.profile,
            total_cost=sum(i[1] * float(i[2]) for i in products_in_order)
        )
        order.products.set(products)
        data = {
            "orderId": order.pk,
        }
        return Response(data)


class OrderDetail(APIView):
    """Детальная информация о заказе и """
    def get(self, request: Request, pk: int) -> Response:
        """Детальная информация о заказе"""
        qs = Order.objects.get(pk=pk)
        serializer = OrderSerializer(qs)
        data = serializer.data
        return Response(data)

    def post(self, request: Request, pk: int) -> Response:
        """Заполнение данных для заказа"""
        order = Order.objects.get(pk=pk)
        data = request.data
        order.fullName = data['fullName']
        order.phone = data['phone']
        order.email = data['email']
        order.deliveryType = data['deliveryType']
        order.city = data['city']
        order.address = data['address']
        order.paymentType = data['paymentType']
        order.status = 'Ожидает оплаты'
        if data['deliveryType'] == 'express':
            order.total_cost += 50
        else:
            if order.total_cost < 200:
                order.total_cost += 20

        for product in data['products']:
            OrderProduct.objects.get_or_create(
                order_id=order.pk,
                product_id=product['id'],
                count=product['count']
            )

        order.save()

        return Response(request.data, status=200)


class PaymentView(APIView):
    """Заполнение данных на оплату"""
    def post(self, request: Request, pk: int) -> Response:
        order = Order.objects.get(pk=pk)
        order.status = 'Оплачен'
        order.save()
        cart = request.session.get('cart', [])
        cart.clear()
        request.session['cart'] = cart
        request.session.save()
        return Response(request.data, status=200)
