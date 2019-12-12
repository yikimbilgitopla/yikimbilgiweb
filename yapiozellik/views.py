from django.shortcuts import render,redirect
from .models import yapiOzellikModel
from .forms import yapiOzellikModel_Form

def yapiOzellikYeni(request):
    if request.method == "POST":
        forms = yapiOzellikModel_Form(request.POST)
        if forms.is_valid():
            yapiOzellik = forms.save(commit=False)
            yapiOzellik.save()
            return redirect('home')
    else:
        forms = yapiOzellikModel_Form()
    return render(request,'yapiozellik/yeni_yapiOzellik.html',{'form':forms})