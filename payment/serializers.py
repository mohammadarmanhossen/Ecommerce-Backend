from rest_framework import serializers
from .models import *
from product.serializers import *



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, data):
        if data['out_date'] <= data['start_date']:
            raise serializers.ValidationError({"out_date": "Out date must be after start date."})
        return data