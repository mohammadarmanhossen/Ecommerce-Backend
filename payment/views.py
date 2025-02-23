from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from sslcommerz_lib import SSLCOMMERZ

import uuid
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import redirect


from rest_framework import viewsets
from .serializers import OrderSerializer
from .models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PaymentViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def create_payment(self, request):

        user_id = request.data.get('user')
        order_id = request.data.get("order_id")
        total_amount = request.data.get('total_amount')

        user = None
        if user_id:
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({"error": "Invalid user ID"}, status=400)

        tran_id = str(uuid.uuid4())[:10]

        settings = {
            'store_id': 'arman679a8128a9e35',
            'store_pass': 'arman679a8128a9e35@ssl',
            'issandbox': True,
        }

        sslcz = SSLCOMMERZ(settings)

        post_body = {
            'total_amount': total_amount,
            'currency': "BDT",
            'tran_id': tran_id,
            'success_url': f"https://ecommerce-backend-4yjb.onrender.com/payment/success/{order_id}/",
            'fail_url': "https://ecommerce-backend-4yjb.onrender.com/payment/failed/",
            'cancel_url': "https://ecommerce-backend-4yjb.onrender.com/payment/cancel/",
            'emi_option': 0,
            'cus_name': "arman",
            'cus_email': "arman@gmail.com",
            'cus_phone': "1908349238",
            'cus_add1': "Mirpur, Dhaka",
            'cus_city': "Dhaka",
            'cus_country': "Bangladesh",
            'shipping_method': "NO",
            'multi_card_name': "10304040",
            'num_of_item': 1,
            'product_name': "Test Product",
            'product_category': "Test Category",
            'product_profile': "general",
        }

        try:
            response = sslcz.createSession(post_body)
            if 'GatewayPageURL' not in response:
                return Response({"error": "Payment session creation failed", "details": response}, status=400)
            return Response({'payment_url': response['GatewayPageURL']})
        except Exception as e:
            return Response({"error": "Payment processing failed", "details": str(e)}, status=500)



class PaymentSuccessAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request, order_id):  

        order = Order.objects.filter(id=order_id).first()

        if order:
            order.is_paid = True
            order.save()
            return redirect("https://joyful-begonia-6e2001.netlify.app/order_details.html")
        
        return Response({"error": "Order not found"}, status=404)



class PaymentFailedAPI(APIView):
    permission_classes = [AllowAny]  

    def post(self, request):
        return redirect("https://joyful-begonia-6e2001.netlify.app/order_details.html")


class PaymentCancelAPI(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        return redirect("https://joyful-begonia-6e2001.netlify.app/order_details.html")





