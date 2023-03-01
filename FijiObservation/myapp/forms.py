from django import forms
from django.core.validators import ValidationError
from .models import Parameter,Observation,Station
import os
class UserForm(forms.Form):
    file=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            filename, ext = os.path.splitext(file.name)
            ext = ext.lower()
            if ext not in ['.csv', '.xlsx']:
                raise ValidationError('Unsupported file format.')
        return file
    