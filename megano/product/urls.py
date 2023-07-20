from django.urls import path
from .views import ProductIdAPIView, CreateReviewApiView
from django.views.decorators.cache import cache_page

app_name = 'product'

urlpatterns = [
    # path('api/product/<int:pk>/', cache_page(60*5)(ProductIdAPIView.as_view())),
    path('api/product/<int:pk>/', ProductIdAPIView.as_view()),
    # path('api/product/<int:pk>/reviews', cache_page(60*5)(CreateReviewApiView.as_view())),
    path('api/product/<int:pk>/reviews', CreateReviewApiView.as_view()),

]
