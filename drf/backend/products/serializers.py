from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Product


class ProductSerializer(ModelSerializer):
    
   
    base_price = serializers.SerializerMethodField(read_only=True)
   
    class Meta:
        model = Product
        fields = ["id", "title", "content", "price","base_price"]
    
    def get_base_price(self, obj):
        try:
            return obj.base_price
        except :
            return None
        # if not hasattr(obj, "base_price"):
        #     return None
        # return obj.base_price

class NewProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "content", "price","get_base_price"]