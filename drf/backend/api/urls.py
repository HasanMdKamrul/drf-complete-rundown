from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import api_home, get_all_products

urlpatterns = [
    path('', api_home, name="home"),
    path('auth/', obtain_auth_token, name="auth" ),
    path('allproducts', get_all_products, name="allproducts")
]
