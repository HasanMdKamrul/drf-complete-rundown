from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.serializers import ModelSerializer

from .models import Product


class ProductSerializer(ModelSerializer):
    
    
    url = serializers.SerializerMethodField(read_only=True)
    
   
    base_price = serializers.SerializerMethodField(read_only=True)
   
    class Meta:
        model = Product
        fields = ['url',"id", "title", "content", "price","base_price"]
    
    def get_base_price(self, obj):
        try:
            return obj.base_price
        except :
            return None
        # if not hasattr(obj, "base_price"):
        #     return None
        # return obj.base_price
    
    
    
    def get_url(self, obj):
       
        request = self.context.get("request")
        mywish = self.context.get("mywish")
        
        print(mywish)
        
        if request is None:
            return None
        return reverse("product-detail",kwargs={"pk":obj.pk},request=request)
        
        # return f"/api/products/ultimate/{obj.id}/"

class NewProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "content", "price","get_base_price"]