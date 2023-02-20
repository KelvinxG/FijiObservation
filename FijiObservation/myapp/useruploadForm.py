from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        file=forms.FileField()