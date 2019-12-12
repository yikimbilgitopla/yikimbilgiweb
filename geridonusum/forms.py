from django import forms
from .models import Geri_Donusum

class Geri_Donusum_Form(forms.ModelForm):
    class Meta:
        model = Geri_Donusum
        fields = ("Geri_Donusum",)
        labels = {"Geri_Donusum":"Geri Dönüşüm"}