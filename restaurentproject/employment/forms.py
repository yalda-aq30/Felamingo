from django import forms
from .models import Employment
from phonenumber_field.formfields import PhoneNumberField

class EmploymentForm(forms.ModelForm):
    class Meta:
        model = Employment
        fields = ['full_name', 'email', 'phone_number', 'positions', 'resume', 'message']

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        phone_str = str(phone)
        if phone_str.startswith("0"):
            phone_str = "+98" + phone_str[1:]
        elif not phone_str.startswith("+98"):
            phone_str = "+98" + phone_str
        return phone_str

