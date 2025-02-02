from rest_framework import serializers
from .models import Product
from rest_framework import serializers
from .models import Product, Review

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Or specify the fields you want like: ['id', 'name', 'price', 'stock']



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_rating(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError("Rating must be an integer.")
        return value


        