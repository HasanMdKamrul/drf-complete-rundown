from decimal import Decimal

from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="product-detail",lookup_field="pk")
    title = serializers.CharField(read_only=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    price_changed = serializers.SerializerMethodField(read_only=True)
    
    def get_price_changed(self, obj):
        return Decimal(obj.price) * Decimal(0.3)

class PublicUserSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    # other_products = serializers.SerializerMethodField(read_only=True)
    
    # def get_other_products(self, obj):
    #     user = obj
    #     products_data = user.product_set.all()[0:2]
    #     return ProductSerializer(products_data, many=True, context = self.context).data