from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/products')