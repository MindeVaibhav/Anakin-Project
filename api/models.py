from django.db import models
import string
import random

def generate_unique_id():
    length = 10
    while True:
        id = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Company.objects.filter(company_id=id).count() == 0:
             break

        return id

# Create your models here.
class Company(models.Model):
    company_id = models.CharField(max_length=10, default=generate_unique_id, unique=True)
    b_email = models.CharField(max_length=10, default="")
    b_password = models.CharField(max_length=10, default="")
    # models.BooleanField, models.IntegerField

class Retailer(models.Model):
    retailer_id = models.CharField(max_length=10, default="", unique=True)
    r_password = models.CharField(max_length=10, default="")

class Store(models.Model):
    store_id = models.CharField(max_length=10, default="", unique=True)
    retailer = models.ForeignKey(Retailer, models.CASCADE)

class Product(models.Model):
    product_id = models.CharField(max_length=10, default="", unique=True)
    product_image = models.CharField(max_length=10, default="")
    price = models.FloatField()
    promotions = models.FloatField()
    store_id = models.ForeignKey(Store, models.CASCADE)

