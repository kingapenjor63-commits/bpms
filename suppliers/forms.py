from django import forms
from .models import CompanyContact

class CompanyContactForm(forms.ModelForm):
    class Meta:
        model = CompanyContact
        fields = [
            'company_name',
            'country',
            'contact_person_name',
            'contact_no',
            'email_id',
            'department',
            'remarks',
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter country'}),
            'contact_person_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any additional notes'}),
        }