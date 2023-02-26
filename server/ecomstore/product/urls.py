from django.urls import path
from .views import products


urlpatterns = [
    path('product/all', products, name="products")
]