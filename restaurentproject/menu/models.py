from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100) 
    def __str__(self):
        return self.name
    
class menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(null=True , blank=True , max_digits=7 , decimal_places=0)
    description = models.TextField(null=True , blank=True) 
    available = models.BooleanField(default=True)  
    category = models.ForeignKey(Category , on_delete=models.CASCADE , null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

def __str__(self):
        return self.name