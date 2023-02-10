from django.urls import path

# from rest_framework.authtoken.views import obtain_auth_token
from .authentication import CustomAuthToken
from .views import PreDataApiView

urlpatterns = [
   
    path('auth/', CustomAuthToken.as_view(), name="auth" ),
    path('predata/', PreDataApiView.as_view(), name="predata")
]
