
from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Product
def showcategories(request):
    cat=Category.objects.all()
    return render(request,"shop.html",{'c':cat})
def showproducts(request,category=None):
   if category:
     categories = get_object_or_404(Category, slug=category)
     products = Product.objects.all().filter(category=categories)
   return render(request,'Product_detail.html',{'product':products})
# Create your views here.
