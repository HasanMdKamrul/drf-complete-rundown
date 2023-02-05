from rest_framework.generics import  RetrieveAPIView, CreateAPIView,ListCreateAPIView,RetrieveUpdateAPIView

from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny


class ProductDetailApiView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_api_view = ProductDetailApiView.as_view()

class ProductUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_update_api_view = ProductUpdateApiView.as_view()

class ProductCreateApiView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)
        
product_create_api_view = ProductCreateApiView.as_view()


class ProductListCreateApiView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)
        
product_list_create_api_view = ProductListCreateApiView.as_view()


