from django import forms
from .models import Parameter,Observation,Station
class UserForm(forms.Form):
    file=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))