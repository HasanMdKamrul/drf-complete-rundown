from products.viewsets import ProductTestViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter() # DefaultRouter is a class and router is an instance of that class

router.register('productsviewset', ProductTestViewSet, basename='products') # register is a method of DefaultRouter class
urlpatterns = router.urls