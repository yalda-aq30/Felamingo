from django.shortcuts import render
from .models import menu 
# Create your views here.

def index(request):
    available_products = menu.objects.filter(available = True) 
    context = {
        'available_product' : available_products
    }
    return render(request ,'menu/index.html' , context)   