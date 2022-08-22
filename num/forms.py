from django import forms
from .models import Prime


class PrimeForm(forms.ModelForm):
    class Meta:
        model = Prime
        fields = ["name", "fnum", "lnum"]
