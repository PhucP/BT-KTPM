from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
import requests

# Create your views here.
def product_list(request):
    response = requests.get('http://127.0.0.1:8000/product/all')

    if response.status_code == 200:
        plist = response.json()
        return render(request, 'index.html', {'products': plist})
    return Response(response.data, status=status.HTTP_404_NOT_FOUND)