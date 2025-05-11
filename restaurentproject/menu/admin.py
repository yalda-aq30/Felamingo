from django.contrib import admin
from .models import menu , Category
# Register your models here.
@admin.register(menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name' , 'price' , 'description' , 'available') 

@admin.register(Category) 
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) 