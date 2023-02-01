from django.urls import path

from .views import api_home, get_all_products

urlpatterns = [
    path('', api_home, name="home"),
    path('allproducts', get_all_products, name="allproducts")
]
