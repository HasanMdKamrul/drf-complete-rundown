from api.serialisers import PublicUserSerialiser
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.serializers import ModelSerializer

from .models import Product
from .validator import unique_title_validator, validate_title_with_hello


class ProductSerializer(ModelSerializer):
    
    user = PublicUserSerialiser(read_only=True)
    
    my_user_data = serializers.SerializerMethodField(read_only=True)
    
    url = serializers.HyperlinkedIdentityField(view_name="product-detail",lookup_field="pk")
    
    edit_url = serializers.SerializerMethodField(read_only=True)
    
    relative_url = serializers.SerializerMethodField(read_only=True)
    
   
    base_price = serializers.SerializerMethodField(read_only=True)
    
    email = serializers.EmailField(write_only=True)
   
   
   
    class Meta:
        model = Product
        fields = ["user",'url','edit_url','relative_url',"email","id", "title", "content", "price","base_price","my_user_data"]
        
    def get_my_user_data(self, obj):
        if obj.user.email == "":
            return {
            "username": obj.user.username,
            "email": "No email",
        }
        return {
            "username": obj.user.username,
            "email": obj.user.email,
        }
    
    title = serializers.CharField(validators=[validate_title_with_hello,unique_title_validator])
    
    # ** Custom validation of the field **
    
    # def validate_title(self, value):
    #     queryset = Product.objects.filter(title__iexact=value)
    #     if queryset.exists():
    #         raise serializers.ValidationError(f"Title {value} already exists")
    #     return value.upper()
    
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