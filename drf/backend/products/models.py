from decimal import *

from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL

CATEGORY_CHOICES = [
    ('Like New', 'Like New'),
    ('Battery Health', 'Battery Health'),
    ('Featured', 'Featured'),
]

# class Category(models.Model):
#     LIKE_NEW = 'Like New'
#     BATTERY_HEALTH = 'Battery Health'
#     FEATURED = 'Featured'
#     CATEGORY_CHOICES = [
#         (LIKE_NEW, 'Like New'),
#         (BATTERY_HEALTH, 'Battery Health'),
#         (FEATURED, 'Featured'),
#     ]
#     name = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default=LIKE_NEW)
#     category_exists = models.BooleanField(default=True)
    
#     def __str__(self):
#         return self.name
        
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1);
    title = models.CharField(max_length=120);
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000, default=9.99)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='Like New')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def discounted_price(self):
        price = Decimal(self.price) * Decimal(0.9)
        return "{:.2f} {}".format(price , "USD")
    
    def get_base_price(self):
        return 222.22


