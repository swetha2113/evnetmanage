from django import forms
from django.forms import fields
from .models import comment


class commentform(forms.ModelForm):
    
    class Meta:
        model=comment
        fields=('content',)
