from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'

class Product(models.Model):
    class Meta:
        db_table = 'product'
    name = models.CharField(max_length=100)
    description = models.TextField(default='This field is for product description')
    image = models.CharField(max_length=100, default='D:/School stuffs/P1/images/capacitor.jpg')
    quantity = models.IntegerField(default=10)
    price = models.IntegerField()
    manufacturer = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)


