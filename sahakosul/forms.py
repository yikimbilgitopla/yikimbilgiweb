from django import forms
from .models import SahaModel

class SahaModel_Form(forms.ModelForm):
    class Meta:
        model = SahaModel
        fields = ("sahaGuvenlik",)
        labels = {"sahaGuvenlik":"Saha Güvenlik"}