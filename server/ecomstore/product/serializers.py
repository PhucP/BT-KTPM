from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # this is the model that is being serialized
        fields = ('id', 'name', 'price', 'manufacturer', 'image', 'description', 'categories')
