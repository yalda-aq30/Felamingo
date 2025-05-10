from django.contrib import admin
from .models import menu 
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name' , 'price' , 'description' , 'available') 