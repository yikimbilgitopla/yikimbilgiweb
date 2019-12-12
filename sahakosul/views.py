from django.shortcuts import render,redirect
from .models import SahaModel
from .forms import SahaModel_Form

def sahaYeni(request):
    if request.method == "POST":
        forms = SahaModel_Form(request.POST)
        if forms.is_valid():
            saha = forms.save(commit=False)
            saha.save()
            return redirect('saha_detay',pk = saha.pk)
    else:
        forms = SahaModel_Form()
    return render(request,'sahaKosul/yeni_sahaKosul.html',{'form':forms})