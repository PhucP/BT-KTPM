from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer  # this is the model that is being serialized
        fields = ('username', 'password', 'name', 'address', 'phone_number', 'personal_id')