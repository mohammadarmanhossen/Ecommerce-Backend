from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product',views.ProductViewSet)
router.register('review', views.ReviewViewSet)
router.register('Brand', views.BrandViewSet)
router.register('Cart', views.CartViewSet )

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:  # Serve media files only in development
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




