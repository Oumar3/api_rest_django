from rest_framework import serializers
from  productapi.models import Product

class ProductSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'