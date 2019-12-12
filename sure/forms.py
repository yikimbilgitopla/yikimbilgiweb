from django import forms
from .models import sureModel

class sureModel_Form(forms.ModelForm):
    class Meta:
        model = sureModel
        fields = ("sahaHazirligi","yikimSureci")
        labels = {"sahaHazirligi":"Saha Hazırlığı",
        "yikimSureci":"Yıkım Süreci",}