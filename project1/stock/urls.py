from django.urls import include, path
from rest_framework import routers

from stock.views import CategoryViewSet, ProductViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
   path('api/', include(router.urls)),
]

