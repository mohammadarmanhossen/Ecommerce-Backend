# from rest_framework import viewsets
# from .models import Product,Keybord,Headphone,Review,Brand
# from .serializers import ProductSerializer,KeybordSerializer,HeadphoneSerializer,ReviewSerializer,BrandSerializer
# from rest_framework import viewsets, filters
# from django_filters.rest_framework import DjangoFilterBackend



# class BrandViewSet(viewsets.ModelViewSet):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filterset_fields = ['brand'] 
#     search_fields = ['name', 'description'] 


# class KeybordViewSet(viewsets.ModelViewSet):
#     queryset = Keybord.objects.all()
#     serializer_class = KeybordSerializer
#     filterset_fields = ['brand'] 
#     search_fields = ['name', 'description'] 

# class HeadphoneViewSet(viewsets.ModelViewSet):
#     queryset = Headphone.objects.all()
#     serializer_class =HeadphoneSerializer
#     filterset_fields = ['brand'] 
#     search_fields = ['name', 'description'] 


    
# class ReviewViewSet(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer







from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Keybord, Headphone, Review, Brand
from .serializers import ProductSerializer, KeybordSerializer, HeadphoneSerializer, ReviewSerializer, BrandSerializer


class BaseViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['brand']
    search_fields = ['name', 'description']

    def get_queryset(self):
        return super().get_queryset().select_related("brand").prefetch_related("review_set")


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.select_related("brand").prefetch_related("review_set").all()
    serializer_class = ProductSerializer

class KeybordViewSet(BaseViewSet):
    queryset = Keybord.objects.select_related("brand").prefetch_related("review_set").all()
    serializer_class = KeybordSerializer

class HeadphoneViewSet(BaseViewSet):
    queryset = Headphone.objects.select_related("brand").prefetch_related("review_set").all()
    serializer_class = HeadphoneSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related("product", "keybord", "headphone").all()
    serializer_class = ReviewSerializer
