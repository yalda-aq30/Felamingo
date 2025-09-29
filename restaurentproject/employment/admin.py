from django.contrib import admin
from .models import Employment 


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'positions']  # ستون‌های لیست
    search_fields = ['full_name', 'email', 'phone_number']  # جستجو
    
