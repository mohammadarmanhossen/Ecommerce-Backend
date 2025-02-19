

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, OrderViewSet, PaymentSuccessAPI, PaymentFailedAPI, PaymentCancelAPI

router = DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='payment')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('payment/success/<int:order_id>/', PaymentSuccessAPI.as_view(), name='payment-success'),
    path('payment/failed/', PaymentFailedAPI.as_view(), name='payment-failed'),
    path('payment/cancel/', PaymentCancelAPI.as_view(), name='payment-cancel'),
]


