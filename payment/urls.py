from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, PaymentSuccessAPI, PaymentFailedAPI, PaymentCancelAPI  

router = DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
    path('payment/success/', PaymentSuccessAPI.as_view(), name='payment-success'),
    path('payment/failed/', PaymentFailedAPI.as_view(), name='payment-failed'),
    path('payment/cancel/', PaymentCancelAPI.as_view(), name='payment-cancel'),
]
