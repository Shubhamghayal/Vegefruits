from django.urls import path
from .views import add_cart,cart
from shop.views import showcategories


urlpatterns = [
    path('cart/', cart, name="cart"),
    path('add_cart/<int:product_id>', add_cart, name="add_cart"),
    path('product_detail/',showcategories,name="shopping"),

]
