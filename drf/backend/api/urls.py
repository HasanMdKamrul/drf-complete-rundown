from django.urls import path

# from rest_framework.authtoken.views import obtain_auth_token
from .authentication import CustomAuthToken
from .views import api_home, get_all_products

urlpatterns = [
    path('', api_home, name="home"),
    path('auth/', CustomAuthToken.as_view(), name="auth" ),
    path('allproducts', get_all_products, name="allproducts")
]
