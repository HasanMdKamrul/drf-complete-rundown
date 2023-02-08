from rest_framework.generics import  RetrieveAPIView, CreateAPIView,ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView

from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductDetailApiView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_api_view = ProductDetailApiView.as_view()

class ProductUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_update(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)

product_update_api_view = ProductUpdateApiView.as_view()

class ProductDeleteApiView(DestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_destroy(self, instance):
        print("Deleting")
        print(instance)
        if instance:
            instance.delete()
        else:
            return Response({"message":"Product not found"},status=404)
          
        
        
product_delete_api_view = ProductDeleteApiView.as_view()

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

@api_view(['GET','POST','PUT','DELETE'])
def get_all_operations(request,*args,**kwargs):
    # ** get all products
    if request.method == 'GET':
        pk = kwargs.get('pk') 
        if pk is not None:
            product = Product.objects.filter(pk=pk)
            serializer = ProductSerializer(product,many=True)
            if serializer.data:
                return Response(serializer.data)
            return Response({"message":"Product not found"},status=404)     
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products,many=True)
            return Response(serializer.data)     
        
    # ** create new product
    
    if request.method == 'POST':
        new_product = request.data
        serializer = ProductSerializer(data=new_product)
        if serializer.is_valid():
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
                serializer.save(content=content)
                return Response(serializer.data)
            
        return Response(serializer.errors)
    
    # # ** update product
    
    if request.method == 'PUT':
        updated_data = request.data
        pk = kwargs.get('pk')
        object_to_update = Product.objects.filter(pk=pk).first()
        serializer = ProductSerializer(object_to_update,updated_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
        return Response(serializer.errors)
        
        
                
    # # ** delete product
    
    if request.method == 'DELETE':
        pk = kwargs.get('pk')
        object_to_delete = Product.objects.filter(pk=pk).first()
        if object_to_delete is not None:
            object_to_delete.delete()
            return Response({"message":"Product deleted successfully", "success" : True},status=200)
       
        
       
        # return JsonResponse(serializer.errors)
        
    
