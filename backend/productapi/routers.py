from rest_framework.routers import DefaultRouter, SimpleRouter
from productapi.api import viewset

router = DefaultRouter()
router.register('product/',viewset.Crud_viewsets_product,basename='product')
urlpatterns = router.urls