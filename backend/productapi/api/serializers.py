from rest_framework import serializers
from  productapi.models import Product

class ProductSerialiser(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = Product
        fields = '__all__'


    def validate(self, attrs):
        return super().validate(attrs)

    def validate_name(self,value):
        if len(value) < 3:
            raise ValueError('Error name len est is short')
        return value
