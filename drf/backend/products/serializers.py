from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Product


class ProductSerializer(ModelSerializer):
    
    my_discount = serializers.SerializerMethodField(read_only=True)
    annual_discount_price = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ["id", "title", "content", "price","sale_price","my_discount","annual_discount_price"]
        
    def get_my_discount(self,obj):
        return obj.get_discount()
    
    def get_annual_discount_price(self,obj):
        return obj.get_annual_price()