from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'id': 'name', 'class': 'form-control', 'placeholder': 'Name', 'required': 'required'
    }))
    email = forms.EmailField(validators=[EmailValidator()], widget=forms.EmailInput(attrs={
        'id': 'email', 'class': 'form-control', 'placeholder': 'Email', 'required': 'required'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'message', 'class': 'form-control', 'placeholder': 'Message', 'rows': 5, 'required': 'required'
    }))