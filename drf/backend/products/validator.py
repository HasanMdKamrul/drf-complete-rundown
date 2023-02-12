from rest_framework import serializers, validators

from .models import Product


def validate_title_with_hello(value):
    
    if "hello"  in value.lower():
        raise serializers.ValidationError("Title cannot contain hello")
    return value


unique_title_validator = validators.UniqueValidator(queryset=Product.objects.all(), message="Title already exists" , lookup="iexact")