from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer


@api_view(['GET'])
def customers(request):
    snippets = Customer.objects.all()
    serializer = CustomerSerializer(snippets, many=True)
    return Response(serializer.data)

