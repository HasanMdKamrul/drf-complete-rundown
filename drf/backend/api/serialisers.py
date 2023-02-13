from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()
from products.models import Product

# class CategorySerializer(serializers.Serializer):
#     name = serializers.CharField(read_only=True)
#     category_exists = serializers.BooleanField(read_only=True)
    
# class MySecondProductSerializer(serializers.ModelSerializer):
    
#     # category = CategorySerializer(read_only=True)
    

#     class Meta:
#         model = Product
#         fields = [
#             'title',
#             'content',
#             'price',
#             # 'category',
#         ]

# class PublicUserSerialiser(serializers.Serializer):
  
#     username = serializers.CharField(read_only=True)
#     id = serializers.IntegerField(read_only=True)
    # products = serializers.SerializerMethodField(read_only=True)
    
    # def get_products(self, obj):
    #     user = obj
    #     qs = Product.objects.filter(user=user)
    #     return MySecondProductSerializer(qs, many=True).data
