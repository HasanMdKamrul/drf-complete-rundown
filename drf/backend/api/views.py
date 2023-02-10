import json

from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.mixins import IsStaffEditorPermissionMixin
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

# import jsonparser

pre_data = {
    "success" : True,
    "message" : "Home Api Enabled"
}

class PreDataApiView(IsStaffEditorPermissionMixin,ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
       
   
        
    



# @api_view(['GET'])
# def get_all_products(request,*args,**kwargs):
#     data = {}
#     # count = Product.objects.all().count() + 1
#     # ** New data created at every request
#     # Product.objects.create(id=count,title="Product",content="New Content",price=123.45)
#     # ** Geting random object from the database (model data is not serialised)
#     model_data = Product.objects.all().order_by('?').first()
#     serialised_data = ProductSerializer(model_data)
#     return Response(serialised_data.data)
    
  
  
  # def get_all_products(request,*args,**kwargs):
#     data = {}
#     count = Product.objects.all().count() + 1
#     # ** New data created at every request
#     Product.objects.create(id=count,title="Product",content="New Content",price=123.45)
#     # ** Geting random object from the database (model data is not serialised)
#     model_data = Product.objects.all().order_by('?').first()
#     # model_data = Product.objects.all()
#     if model_data:
#        data = model_to_dict(model_data, fields=['id','title'])
#     return JsonResponse(data=data,safe=False)
    
    # if model_data:
    #     data = ProductSerializer(model_data).data
    
    # return JsonResponse(serialised_data.data,safe=False)
        
   
    # # model_data = Product.objects.all()
    # if model_data:
    #    data = model_to_dict(model_data)
    # return JsonResponse(data=data)
        

