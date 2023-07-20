from django.urls import path
from django.views.decorators.cache import cache_page


from .views import (
    CategoriesListAPIView, CatalogListAPIView, ProductPopularListAPIView,
    SaleAPIView,
    ProductLimitedListAPIView
)

app_name = 'category'

urlpatterns = [
    path('api/categories/', CategoriesListAPIView.as_view()),
    path('api/catalog/', CatalogListAPIView.as_view()),
    path('api/products/popular/', ProductPopularListAPIView.as_view()),
    path('api/products/limited/', ProductLimitedListAPIView.as_view()),
    path('api/banners/', ProductLimitedListAPIView.as_view()),
    path('api/sales/', SaleAPIView.as_view()),
]

