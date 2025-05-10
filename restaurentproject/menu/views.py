from django.shortcuts import render
from .models import menu
# Create your views here.

def index(request):
    return render(request ,'menu/index.html')   