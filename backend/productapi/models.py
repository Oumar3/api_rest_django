from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)


    def get_absolute_url(self):
        return reverse("detail_product", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return self.name