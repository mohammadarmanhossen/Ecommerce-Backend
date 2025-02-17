from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product',views.ProductViewSet)
router.register('keybord',views.KeybordViewSet)
router.register('headphone',views.HeadphoneViewSet)
router.register('review', views.ReviewViewSet)
router.register('Brand', views.BrandViewSet)
router.register('cart', views.CartViewSet )

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG: 
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




