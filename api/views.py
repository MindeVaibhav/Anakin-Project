from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView 
from rest_framework.response import Response
from .models import Company, Retailer, Store, Product
from .serializer import CompanySerializer, RetailerSerializer, StoreSerializer, ProductSerializer, CreateCompanySerializer


# Create your views here.

class CompanyView(generics.ListAPIView):
     queryset = Company.objects.all()
     serializer_class = CompanySerializer

class CreateCompantView(APIView):
     serializer_class = CreateCompanySerializer
     def post(self, request, format=None):
          if not self.request.session.exists(self.request.session.session_key):
               self.request.session.create()
          serializer = self.serializer_class(data=request.data)
          if serializer.is_valid():
               b_email = serializer.data.b_email
               b_password = serializer.data.b_password
          company = Company(id="", b_email=b_email, b_password=b_password)
          company.save()
          return Response(CompanySerializer(company).data, status=status.HTTP_201_CREATED)

class RetailerView(generics.ListAPIView):
     queryset = Retailer.objects.all()
     serializer_class = RetailerSerializer

class StoreView(generics.ListAPIView):
     queryset = Store.objects.all()
     serializer_class = StoreSerializer

class ProductView(generics.ListAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
