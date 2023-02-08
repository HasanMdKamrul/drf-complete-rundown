from django.urls import path

from .views import (get_all_operations, product_create_api_view,
                    product_delete_api_view, product_detail_api_view,
                    product_list_create_api_view, product_mixin_operations,
                    product_update_api_view, productDeleteAndRetrive,
                    productUltimate)

urlpatterns = [
    path('<int:pk>/', product_detail_api_view, name='product-detail'),
    path('<int:pk>/delete/', productDeleteAndRetrive, name='product-delete-retrieve'),
    path('<int:pk>/update/', product_update_api_view, name='product-update'),
    # path('<int:pk>/delete/', product_delete_api_view, name='product-delete'),
    path('', product_list_create_api_view, name='product-create'),
    path('alloptions/', get_all_operations, name='product-all-options'),
    path('alloptions/<int:pk>/', get_all_operations, name='product-all-options-id'),
    path('mixins/', product_mixin_operations, name='product-mixin-operations'),
    path('mixins/<int:pk>/', product_mixin_operations, name='product-mixin-operations-retrieve'),
    path('ultimate/', productUltimate, name='product-ultimate'),
    path('ultimate/<int:pk>/', productUltimate, name='product-ultimate-retrieve'),
    
]