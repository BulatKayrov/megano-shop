from .views import OrderListApiView, OrderDetail, PaymentView
from django.urls import path


app_name = 'orders'

urlpatterns = [
    path("api/orders", OrderListApiView.as_view()),
    path("api/order/<int:pk>", OrderDetail.as_view()),
    path("api/payment/<int:pk>", PaymentView.as_view()),
]
