from django.urls import path
from .views import BasketOfProductsView

app_name = 'cart'

urlpatterns = [
    path('api/basket', BasketOfProductsView.as_view()),
]
