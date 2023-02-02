from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120);
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    
    def __str__(self):
        return self.title
    
    @property
    def sale_price(self):
        return "%.3f" %(float(self.price) * 0.7)
    
    def get_discount(self):
        return 1223
    
    def get_annual_price(self):
        return self.price * 12