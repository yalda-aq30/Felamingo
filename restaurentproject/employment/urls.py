from . import views
from django.contrib import admin
from django.urls import path


app_name = 'employment'
urlpatterns = [
    path('', views.employment_view, name='employment'),  
] 
