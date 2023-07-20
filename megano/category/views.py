from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from product.models import Products
from .models import Category
from .serializers import CategorySerializers, CatalogProductSerializers, SalesSerializers
from .pagination import CustomPagination
import logging
from .filter_products import ProductFilter

log = logging.getLogger(__name__)


class CategoriesListAPIView(generics.ListAPIView):
    """View categories and subcategories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CatalogListAPIView(generics.ListAPIView):
    """Catalog products"""
    queryset = Products.objects.all()
    serializer_class = CatalogProductSerializers
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter


class ProductPopularListAPIView(generics.ListAPIView):
    """View popular products"""
    queryset = Products.objects.filter(popular=True)
    serializer_class = CatalogProductSerializers


class ProductLimitedListAPIView(generics.ListAPIView):
    """View limited products"""
    queryset = Products.objects.filter(popular=True)
    serializer_class = CatalogProductSerializers


class SaleAPIView(generics.ListAPIView):
    """View discounted products"""
    # queryset = Products.objects.prefetch_related('tags').select_related('category', 'specification').filter(sale=True).all()
    queryset = Products.objects.filter(sale=True)
    serializer_class = SalesSerializers
    pagination_class = CustomPagination
