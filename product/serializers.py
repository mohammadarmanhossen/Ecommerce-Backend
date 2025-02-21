from rest_framework import serializers
from .models import Product
from rest_framework import serializers
from .models import Product,Keybord,Headphone,Review,Brand
from rest_framework import serializers




class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name', read_only=True) 

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'image', 'brand']



class KeybordSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name')

    class Meta:
        model = Keybord
        fields = ['id', 'name', 'description', 'price', 'stock', 'image', 'brand']



class HeadphoneSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name')

    class Meta:
        model = Headphone
        fields = ['id', 'name', 'description', 'price', 'stock', 'image', 'brand']




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields ="__all__"






