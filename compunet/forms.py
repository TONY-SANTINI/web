from django.forms import ModelForm
from django import forms
class ContactoForm(forms.Form):
    correo=forms.EmailField()
    mensaje=forms.CharField()
    mensaje=forms.CharField(widget=forms.Textarea)