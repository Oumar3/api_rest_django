from productapi.api.serializers import ProductSerialiser
from rest_framework.viewsets import ModelViewSet
from productapi.models import Product
from rest_framework import generics

class Crud_viewsets_product(ModelViewSet):
    serializer_class = ProductSerialiser
    queryset = Product.objects.all()

    

