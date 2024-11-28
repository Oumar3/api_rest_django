from django.urls import path,include
from . import views
from productapi.api import api, ApiViews
urlpatterns = [
    path('',views.api_views_product),
    path('product',api.product_view_api),
    path('product/<int:pk>',api.product_view_api,name='detail_product'),
    path('',include('productapi.routers')),
    path('v2/product',ApiViews.ProductAPIVIEWS.as_view()),
    path('v2/product/<int:pk>',ApiViews.ProductDetailAPIView.as_view(),name='detail_product'),
]
