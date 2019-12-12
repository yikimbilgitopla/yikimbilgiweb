from django import forms
from .models import yapiOzellikModel

class yapiOzellikModel_Form(forms.ModelForm):
    class Meta:
        model = yapiOzellikModel
        fields = ("Yukseklik",
        "Tip",
        "Stabilite",
        "yikimSeviyesi",
        "yapininKullanimi",
        )
        labels = {"Yukseklik":"Yükseklik",
        "Tip":"Tip",
        "Stabilite":"Stabilite",
        "yikimSeviyesi":"Yıkım Seviyesi",
        "yapininKullanimi":"Yapının Kullanımı",
        }