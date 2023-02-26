from django.urls import path
from .views import *


urlpatterns = [
    path('customer/all', customers, name="customers")
]