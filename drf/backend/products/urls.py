from django.urls import path
from .views import product_detail_api_view,product_create_api_view,product_list_create_api_view,product_update_api_view

urlpatterns = [
    path('<int:pk>/', product_detail_api_view, name='product-detail'),
    path('<int:pk>/update/', product_update_api_view, name='product-update'),
    path('', product_list_create_api_view, name='product-create'),
]