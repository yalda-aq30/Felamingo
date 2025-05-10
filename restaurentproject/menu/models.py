from django.db import models

# Create your models here.

class menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(null=True , blank=True , max_digits=7 , decimal_places=0)
    description = models.TextField(null=True , blank=True) 
    available = models.BooleanField(default=True)  