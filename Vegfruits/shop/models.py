from django.db import models
from category.models import Category
class Product(models.Model):
    product_name=models.CharField(max_length=20,unique=True)
    price=models.FloatField()
    images=models.ImageField(upload_to='images')
    stock=models.IntegerField()
    is_avialable=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
# Create your models here.
    def __str__(self):
        return self.product_name
