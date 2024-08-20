# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Contact, Product, ENetwork

class ContactSerializer(serializers.ModelSerializer):
    """серилизатор для модели класса Contact"""
    class Meta:
        model = Contact
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    """серилизатор для модели класса Product"""
    class Meta:
        model = Product
        fields = '__all__'

class ENetworkSerializer(serializers.ModelSerializer):
    """серилизатор для модели класса ENetwork"""
    class Meta:
        model = ENetwork
        fields = '__all__'

class ENetworkUpdateSerializer(serializers.ModelSerializer):
    """серилизатор для обновления модели класса ENetwork"""
    class Meta:
        model = ENetwork
        fields = ['name', 'contact', 'products', 'supplier', 'level_network']
        extra_kwargs = {
            'debt': {'read_only': True},
        }