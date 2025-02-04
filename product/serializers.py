from rest_framework import serializers
from .models import Product
from rest_framework import serializers
from .models import Product,Keyboard,Headphone,Review,Brand

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = '__all__' 

class HeadphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headphone
        fields = '__all__' 

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'