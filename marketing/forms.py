# marketing/forms.py

from django import forms
from .models import ContestEntry

class ContestForm(forms.ModelForm):
    class Meta:
        model = ContestEntry
        fields = ['nombre', 'email', 'anime_fav']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'anime_fav': forms.TextInput(attrs={'class': 'form-control'}),
        }
