from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, ProductViewSet, ENetworkViewSet


router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'products', ProductViewSet)
router.register(r'enetwork', ENetworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
