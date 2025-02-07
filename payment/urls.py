from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
router = DefaultRouter()

urlpatterns = [
    path('', views.PaymentAPI.as_view(), name='payment'),
]



