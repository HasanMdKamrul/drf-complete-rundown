
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/',include('api.urls')),
    path('api/products/', include('products.urls')),
    path('api/v2/', include('cfehome.routers')),
]
