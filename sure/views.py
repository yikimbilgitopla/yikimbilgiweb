from django.shortcuts import render,redirect
from .models import sureModel
from .forms import sureModel_Form

def sureYeni(request):
    if request.method == "POST":
        forms = sureModel_Form(request.POST)
        if forms.is_valid():
            sure = forms.save(commit=False)
            sure.save()
            return redirect('sure_detay',pk = sure.pk)
    else:
        forms = sureModel_Form()
    return render(request,'sure/yeni_sure.html',{'form':forms})