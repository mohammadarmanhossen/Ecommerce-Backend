from rest_framework import serializers
from .models import Product
from rest_framework import serializers
from .models import Product,Review,Brand,Cart

class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'image', 'brand']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields ="__all__"



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields ="__all__"



