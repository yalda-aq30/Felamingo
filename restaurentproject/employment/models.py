from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Employment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(region="IR")  
    JOB_CHOICES = [
        ('HC','Head Chef'),
        ('WA','Waiter'),
        ('RM','Restaurant Manager'),
        ('CS','Customer Support'),
    ] 
    positions = models.CharField(max_length=2, choices=JOB_CHOICES)   
    resume = models.FileField(upload_to='resumes/', blank=True) 
    message = models.TextField(blank=True) 

    def __str__(self):
        return self.full_name 
    

