from rest_framework import serializers
from  productapi.models import Product

class ProductSerialiser(serializers.ModelSerializer):
    detail_product = serializers.HyperlinkedIdentityField(view_name='detail_product',lookup_field='pk')
    name = serializers.CharField()
    class Meta:
        model = Product
        fields = ['name','content','price','detail_product']


    def validate(self, attrs):
        return super().validate(attrs)

    def validate_name(self,value):
        if len(value) < 3:
            raise ValueError('Error name len est is short')
        return value
