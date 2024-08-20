# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .models import Contact, Product, ENetwork
from .permissions import IsActiveUser
from .serializers import ContactSerializer, ProductSerializer, ENetworkSerializer, ENetworkUpdateSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """Viewset модели класса Contact"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsActiveUser]

class ProductViewSet(viewsets.ModelViewSet):
    """Viewset модели класса Product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]

class ENetworkViewSet(viewsets.ModelViewSet):
    """Viewset модели класса ENetwork"""
    queryset = ENetwork.objects.all()
    serializer_class = ENetworkSerializer
    permission_classes = [IsActiveUser]

    def get_serializer_class(self):
        """проверка на изменение данных экземпляра"""
        if self.request.method == 'PATCH':
            return ENetworkUpdateSerializer
        return super().get_serializer_class()
