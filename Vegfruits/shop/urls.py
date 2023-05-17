from .views import showcategories,showproducts
from django.urls import path

urlpatterns = [

    path('shop/',showcategories,name='shop'),
    path('showproducts/<slug:category>/',showproducts),


]