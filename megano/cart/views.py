from rest_framework.response import Response
from rest_framework.views import APIView
from cart.serializers import BasketSerializer
from product.models import Products


class BasketOfProductsView(APIView):
    """Shopping cart for sessions"""

    def get(self, request) -> Response:
        cart = request.session.get('cart', [])
        for item in cart:  #  удаляем товары кол-во которых меньше 1
            if item['count'] == 0:
                cart.remove(item)
        product_ids = [item['id'] for item in cart]  # Получаем список id товаров
        products = Products.objects.in_bulk(product_ids)  # Получаем все объекты Product вместо цикла для каждого id
        products_list = [products[item_id] for item_id in
                         product_ids]  # Создаем список объектов Product, основанных на полученных объектах
        context = {'cart': cart}
        serializer = BasketSerializer(instance=products_list, many=True, context=context)
        return Response(serializer.data, status=200)

    def post(self, request) -> Response:
        """Добавляем товар в корзину предварительно проверив что корзина есть, иначе создаем"""
        cart = request.session.get('cart', [])
        for item in cart:
            if item['id'] == request.data['id']:
                item['count'] += request.data['count']
                break
        else:
            cart.append({
                'id': request.data['id'],
                'count': request.data['count'],
            })

        request.session['cart'] = cart
        request.session.save()
        context = {'cart': cart}
        # lst: Создаем список экземляров продуктов
        lst = [
            Products.objects.
            select_related('specification', 'specification').
            prefetch_related('tags').
            get(id=item['id']) for item in cart
        ]
        # serializers: сериализируем данные из списка продуктов и
        # передаем контекст корзины для подсчета кол-ва определенных продуктов
        serializers = BasketSerializer(instance=lst, many=True, context=context)
        return Response(serializers.data, status=200)

    def delete(self, request) -> Response:
        """Удаляем товар из корзины и сохраняем изменения"""
        cart = request.session.get('cart', [])
        for item in cart:
            if item['id'] == request.data['id'] and item['count'] > 0:
                if request.data['count'] >= 1:
                    item['count'] -= request.data['count']
                else:
                    cart.remove(item)
            else:
                cart.remove(item)
        request.session['cart'] = cart
        request.session.save()
        context = {'cart': cart}
        # lst: создаем список продуктов
        lst = [
            Products.objects.
            select_related('specification', 'specification').
            prefetch_related('tags').
            get(id=item['id']) for item in cart
        ]
        serializers = BasketSerializer(instance=lst, many=True, context=context)
        return Response(serializers.data, status=200)

