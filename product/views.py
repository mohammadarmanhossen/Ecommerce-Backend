from rest_framework import viewsets
from .models import Product,Review,Brand
from .serializers import ProductSerializer,KeyboardSerializer,HeadphoneSerializer,ReviewSerializer,BrandSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class keyboardViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = KeyboardSerializer

class HeadphoneViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = HeadphoneSerializer

    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

   
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer