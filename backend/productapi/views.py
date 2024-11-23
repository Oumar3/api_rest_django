from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
@csrf_exempt
def api_views_product(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        Product.objects.create(
            name=data.get('name'),
            content=data.get('content'),
            price=data.get('price')
            )
        return JsonResponse(data)
    products = Product.objects.all()
    data = [{'id':product.id,'name':product.name,'content':product.content,'price':product.price} for product in products]
    return JsonResponse(data,safe=False)
