from django.shortcuts import render,redirect
from .models import MaliyetModel
from .forms import MaliyetModel_Form

def maliyetYeni(request):
    if request.method == "POST":
        forms = MaliyetModel_Form(request.POST)
        if forms.is_valid():
            maliyet = forms.save(commit=False)
            maliyet.save()
            return redirect('maliyet_detay',pk = maliyet.pk)
    else:
        forms = MaliyetModel_Form()
    return render(request,'maliyet/yeni_maliyet.html',{'form':forms})