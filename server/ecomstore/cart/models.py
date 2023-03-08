# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from customer.models import Customer
from product.models import Product

class Cart(models.Model):
    CART_STATUS_CHOICES = [
        ('WAIT', 'wait'),
        ('PAID', 'paid'),
        ('SHIP', 'shipping'),
        ('FNSH', 'finished'),
        ('REFU', 'refunded')
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=4, choices=CART_STATUS_CHOICES, default='WAIT')
    products = models.ManyToManyField(Product, through='CartProduct')

class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
