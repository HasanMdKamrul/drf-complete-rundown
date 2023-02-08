from django.urls import path
from .views import product_detail_api_view,product_create_api_view,product_list_create_api_view,product_update_api_view,get_all_operations,product_delete_api_view

urlpatterns = [
    path('<int:pk>/', product_detail_api_view, name='product-detail'),
    path('<int:pk>/update/', product_update_api_view, name='product-update'),
    path('<int:pk>/delete/', product_delete_api_view, name='product-delete'),
    path('', product_list_create_api_view, name='product-create'),
    path('alloptions/', get_all_operations, name='product-all-options'),
    path('alloptions/<int:pk>/', get_all_operations, name='product-all-options-id'),
]