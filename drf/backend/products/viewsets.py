from rest_framework import viewsets
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .mixins import IsStaffEditorPermissionMixin
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(IsAdminUser,IsStaffEditorPermissionMixin,viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductTestViewSet(viewsets.ViewSet):
   
    
    def list(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serialisers = ProductSerializer(queryset,many=True)
        return Response(serialisers.data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serialisers = ProductSerializer(instance)
        return Response(serialisers.data)
    