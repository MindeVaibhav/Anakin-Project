from dataclasses import fields
from pyexpat import model
from statistics import mode
from rest_framework import serializers
from .models import Company, Retailer, Store, Product

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_id', 'b_email', 'b_password')

class CreateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('b_email', 'b_password')

class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ('retailer_id', 'r_password')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('store_id', 'retailer')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_id', 'product_image', 'price', 'promotions', 'store_id')
        
