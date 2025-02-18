from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .import views

from .views import PostCartView

router = DefaultRouter()
router.register('product',views.ProductViewSet)
router.register('keybord',views.KeybordViewSet)
router.register('headphone',views.HeadphoneViewSet)
router.register('review', views.ReviewViewSet)
router.register('Brand', views.BrandViewSet)
router.register('cart', views.CartViewSet )

urlpatterns = [
    path('', include(router.urls)),
    path('cart/', PostCartView.as_view(), name='post_cart'), 
]

if settings.DEBUG: 
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



