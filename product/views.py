from rest_framework import viewsets
from .models import Product,Review,Brand,Cart
from .serializers import ProductSerializer,ReviewSerializer,BrandSerializer,CartSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['brand'] 
    search_fields = ['name', 'description'] 

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

   

