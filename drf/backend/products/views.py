from rest_framework.generics import  RetrieveAPIView

from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer


class ProductDetailApiView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


product_detail_api_view = ProductDetailApiView.as_view()