from django import forms
from .models import tecrubeModel

class tecrubeModel_Form(forms.ModelForm):
    class Meta:
        model = tecrubeModel
        fields = ("yatkinlik","kaynakekipman","uzmanlik",)
        labels = {"yatkinlik":"Yatkınlık",
        "kaynakekipman":"Kaynak Ekipman",
        "uzmanlik":"Uzmanlık",}