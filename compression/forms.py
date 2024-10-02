# forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import fileInput


# Django form that controlls the user inputting a file
class inputFileForm(forms.ModelForm):
    file = forms.FileField(label='')
    class Meta:
        model = fileInput
        fields = ['file']

