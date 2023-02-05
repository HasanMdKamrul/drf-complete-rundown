from django.urls import path
from .views import product_detail_api_view

urlpatterns = [
    path('<int:pk>/', product_detail_api_view, name='product-detail'),
]