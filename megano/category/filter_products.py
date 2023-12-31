from django.db.models import F, Count, Avg, QuerySet
from django_filters import rest_framework as filters

from product.models import Products


class ProductFilter(filters.FilterSet):
    """
    Фильтрация товаров
    """
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    title = filters.CharFilter(field_name='title')
    free_delivery = filters.BooleanFilter(field_name='freeDelivery')

    class Meta:
        model = Products
        fields = ['min_price', 'max_price', 'title', 'free_delivery']

    def filter_queryset(self, queryset) -> QuerySet:
        """
        Проверяем из get запроса какие фильтры к нам пришли и фильтруем
        queryset: модель Products
        """
        queryset = super().filter_queryset(queryset)

        sort = self.request.query_params.get('sort')
        sort_type = self.request.query_params.get('sortType')

        if sort == 'price' and sort_type == 'dec':
            queryset = queryset.order_by('price')
        elif sort == 'date' and sort_type == 'dec':
            queryset = queryset.order_by('-date')
        elif sort == 'reviews' and sort_type == 'dec':
            queryset = queryset.annotate(num_reviews=Count('reviews')).order_by('num_reviews')
        elif sort == 'rating' and sort_type == 'dec':
            queryset = queryset.annotate(avg_rating=Avg('reviews__rate')).order_by('avg_rating')

        min_price = self.request.query_params.get('filter[minPrice]')
        max_price = self.request.query_params.get('filter[maxPrice]')
        title = self.request.query_params.get('filter[name]')
        free_delivery = self.request.query_params.get('filter[freeDelivery]')

        if free_delivery == 'false':
            queryset = queryset.filter(freeDelivery=False)
        elif free_delivery == 'true':
            queryset = queryset.filter(freeDelivery=True)

        if min_price and max_price:
            queryset = queryset.filter(price__range=(min_price, max_price))
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)

        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset
