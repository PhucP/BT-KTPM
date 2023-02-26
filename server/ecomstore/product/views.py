from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def products(request):
    snippets = Product.objects.all()
    serializer = ProductSerializer(snippets, many=True)
    return Response(serializer.data)