from django import forms
from .models import MaliyetModel

class MaliyetModel_Form(forms.ModelForm):
    class Meta:
        model = MaliyetModel
        fields = ("makine","insan_gucu")
        labels = {"makine":"Makine",
                "insan_gucu":"İnsan Gücü"}