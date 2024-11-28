from rest_framework.decorators import api_view
from productapi.models import Product
from .serializers import ProductSerialiser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET','POST','PUT','DELETE'])
def product_view_api(request, pk=None, *args, **kwargs):
    if request.method=='GET':
        if pk is not None:
            product = get_object_or_404(Product,pk=pk)
            context = {'request': request}
            data_serializer = ProductSerialiser(product,context=context)
            return Response(data_serializer.data)
        context={
            'request':request
        }
        products = Product.objects.all()
        data_serializer = ProductSerialiser(products, many=True,context=context)
        return Response(data_serializer.data)

    if request.method=='POST':
        print(request.stream)
        context={'request': request}
        serializer = ProductSerialiser(data=request.data,context=context)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_201_CREATED)
    
    if request.method=='PUT':
        if pk is None:
            return Response({"message":"Pk is none enter is vaide pk"})
        
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerialiser(product,data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    if request.method=='DELETE':
        if pk is None:
            return Response({"message":"Pk is none enter is vaide pk"})
        
        product = get_object_or_404(Product,pk=pk)
        product.delete()        
        return Response({"message":"Product deleted successfully"})
    

