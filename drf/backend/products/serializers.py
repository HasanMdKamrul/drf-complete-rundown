from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.serializers import ModelSerializer

from .models import Product


class ProductSerializer(ModelSerializer):
    
    
    url = serializers.HyperlinkedIdentityField(view_name="product-detail",lookup_field="pk")
    
    edit_url = serializers.SerializerMethodField(read_only=True)
    
    relative_url = serializers.SerializerMethodField(read_only=True)
    
   
    base_price = serializers.SerializerMethodField(read_only=True)
    
    email = serializers.EmailField(write_only=True)
   
    class Meta:
        model = Product
        fields = ['url','edit_url','relative_url',"email","id", "title", "content", "price","base_price"]
    
    def get_base_price(self, obj):
        try:
            return obj.base_price
        except :
            return None
        # if not hasattr(obj, "base_price"):
        #     return None
        # return obj.base_price
        
        
    def get_relative_url(self, obj):
        return f"/api/products/ultimate/{obj.id}/"
    
    def create(self, validated_data):
        # type of validated_data is dict
        print(type(validated_data))
        # print(validated_data["title"])
        email = validated_data.pop("email")
        validated_data["content"] = email
        return super().create(validated_data)
    
    
    def update(self, instance, validated_data):
        email = validated_data.pop("email")
        return super().update(instance, validated_data)
    
    def get_edit_url(self, obj):
       
        request = self.context.get("request")
        
        if request is None:
            return None
        return reverse("product-update",kwargs={"pk":obj.pk},request=request)
        
        # return f"/api/products/ultimate/{obj.id}/"

class NewProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "content", "price","get_base_price"]