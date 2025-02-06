
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from sslcommerz_lib import SSLCOMMERZ
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny



class PaymentAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            tran_id = str(uuid.uuid4())[:10] 

            settings = {
                'store_id': 'arman679a8128a9e35',
                'store_pass': 'arman679a8128a9e35@ssl',
                'issandbox': True, 
            }

            sslcz = SSLCOMMERZ(settings)

            post_body = {
                'total_amount': 5000,
                'currency': "BDT",
                'tran_id': tran_id,
                'success_url': "http://127.0.0.1:8000/payment/success/",
                'fail_url': "http://127.0.0.1:8000/payment/failed/",
                'cancel_url': "http://127.0.0.1:8000/payment/cancel/",
                'emi_option': 0,
                'cus_name':User.username,
                'cus_email':User.email,
                'cus_phone': "01765034196",
                'cus_add1': "Dhaka",
                'cus_city': "Dhaka",
                'cus_country': "Bangladesh", 
                'shipping_method': "NO",
                'multi_card_name': "10304040",
                'num_of_item': 1,
                'product_name': "Test",
                'product_category': "Test Category",
                'product_profile': "general",
            }

            response = sslcz.createSession(post_body)

            if 'GatewayPageURL' not in response:
                return Response({"error": "Payment session creation failed", "details": response}, status=400)

            return Response({'payment_url': response['GatewayPageURL']})

        except Exception as e:
            return Response({"error": str(e)}, status=500)


class PaymentSuccessAPI(APIView):
    def post(self, request):
        return Response({"message": "Payment successful", "data": request.data})

class PaymentFailedAPI(APIView):
    def post(self, request):
        return Response({"message": "Payment failed", "data": request.data})


class PaymentCancelAPI(APIView):
    def post(self, request):
        return Response({"message": "Payment cancelled", "data": request.data})




        

 



