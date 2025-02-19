from rest_framework import viewsets
from .models import Product,Keybord,Headphone,Review,Brand
from .serializers import ProductSerializer,KeybordSerializer,HeadphoneSerializer,ReviewSerializer,BrandSerializer
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


class KeybordViewSet(viewsets.ModelViewSet):
    queryset = Keybord.objects.all()
    serializer_class = KeybordSerializer
    filterset_fields = ['brand'] 
    search_fields = ['name', 'description'] 

class HeadphoneViewSet(viewsets.ModelViewSet):
    queryset = Headphone.objects.all()
    serializer_class =HeadphoneSerializer
    filterset_fields = ['brand'] 
    search_fields = ['name', 'description'] 


    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer




