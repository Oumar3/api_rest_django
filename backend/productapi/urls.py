from django.urls import path
from . import views
from productapi.api import api

urlpatterns = [
    path('',views.api_views_product),
    path('product',api.product_view_api),
    path('product/<int:pk>',api.product_view_api,name='detail_product'),
]
