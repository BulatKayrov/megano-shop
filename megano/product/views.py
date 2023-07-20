from rest_framework.request import Request
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
import logging
from .models import Products, Review
from .serializers import ProductSerializers, ReviewSerializers


log = logging.getLogger(name='Review')


class ProductIdAPIView(generics.RetrieveAPIView):
    """Отображение продуктов"""
    queryset = Products.objects.select_related('category', 'specification').\
        prefetch_related('tags').all()
    serializer_class = ProductSerializers


class CreateReviewApiView(APIView):
    """Создание отзыва"""
    def post(self, request: Request, pk: int) -> Response:
        serializer = ReviewSerializers(data=request.data)
        if serializer.is_valid():
            if not request.user.is_authenticated:
                return Response({'error': 'Пользователь должен быть аутентифицирован'}, status=401)

            Review.objects.create(
                author=request.user,
                product_id=pk,
                text=request.data.get('text'),
                rate=request.data.get('rate')
            )

            reviews = Review.objects.select_related('author', 'product').filter(product_id=pk)
            serializer = ReviewSerializers(reviews, many=True)
            log.info(f'add review: {request.user}')
            return Response(serializer.data, status=200)

        return Response(status=500)
