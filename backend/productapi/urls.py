from django.urls import path
from . import views
from productapi.api import api

urlpatterns = [
    path('',views.api_views_product),
    path('api/',api.product_view_api),
    path('api/<int:pk>',api.product_view_api),
]
