from rest_framework import viewsets
from .models import Product,Keybord,Headphone,Review,Brand,Cart
from .serializers import ProductSerializer,KeybordSerializer,HeadphoneSerializer,ReviewSerializer,BrandSerializer,CartSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, Product
from .serializers import CartSerializer






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

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer





class PostCartView(APIView):

    def post(self, request):
        cart_data = request.data.get('cart', [])
        total_amount = request.data.get('total_amount', 0)

        # Iterate through cart items
        for item in cart_data:
            product_id = item.get('product_id')  # Getting product ID
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_400_BAD_REQUEST)

            # Add item to the cart
            cart_item = Cart(
                user=request.user,  # Associate cart with the current logged-in user
                product=product,
                quantity=item.get('quantity'),
                total_amount=product.price * item.get('quantity'),
                is_paid=False
            )
            cart_item.save()

        return Response({"message": "Cart items added successfully"}, status=status.HTTP_201_CREATED)
