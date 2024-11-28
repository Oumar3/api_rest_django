from rest_framework.views import APIView
from productapi.models import Product
from .serializers import ProductSerialiser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

def checkToriname(product):
    if product.validated_data.get('name') == 'ToriDev':
        return Response({'Message':'le nom ne doit pas etre toridev'})

class ProductAPIVIEWS(APIView):
    def get(self,request,*args, **kwargs):
        product = Product.objects.all()
        serializ = ProductSerialiser(product,many=True)
        return Response(serializ.data)
    
    def post(self,request):
        product = ProductSerialiser(data=request.data)
        if product.is_valid():
            product.save()
            return Response(product.data, status=status.HTTP_201_CREATED)
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)
        
    def get(self,request,pk, *args, **kwargs):
        product = self.get_object(pk)
        serializer = ProductSerialiser(product)
        return Response(serializer.data)
    
    def put(self,request,pk):
        product = self.get_object(pk)
        serialser = ProductSerialiser(product, data=request.data)
        if serialser.is_valid(raise_exception=True):
            checkToriname(serialser)
            serialser.save()
            return Response(serialser.data)
        return Response(serialser.errors)
    
    def delete(self,request,pk):
        product = self.get_object(pk)
        if product:
            product.delete()
            return Response({'message':'deleted successfully'})

