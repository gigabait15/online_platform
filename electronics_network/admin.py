# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Contact, Product, ENetwork


@admin.action(description='Clear debts')
def clear_debt(modeladmin, request, queryset):
    """функция для очиски поля долг"""
    queryset.update(debt=0.00)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(ENetwork)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'level_network', 'contact', 'debt', 'created_at')
    list_filter = ('contact__city',)
    actions = [clear_debt]