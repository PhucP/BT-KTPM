from django.urls import path
from .views import *

urlpatterns = [
    path('home', product_list, name="products")
]