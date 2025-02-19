from rest_framework import serializers
from .models import *
from product.serializers import *



from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','total_amount', 'is_paid']  



