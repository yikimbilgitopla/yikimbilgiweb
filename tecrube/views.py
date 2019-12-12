from django.shortcuts import render,redirect
from .models import tecrubeModel
from .forms import tecrubeModel_Form

def tecrubeYeni(request):
    if request.method == "POST":
        forms = tecrubeModel_Form(request.POST)
        if forms.is_valid():
            tecrube = forms.save(commit=False)
            tecrube.save()
            return redirect('tecrube_detay',pk = tecrube.pk)
    else:
        forms = tecrubeModel_Form()
    return render(request,'tecrube/yeni_tecrube.html',{'form':forms})