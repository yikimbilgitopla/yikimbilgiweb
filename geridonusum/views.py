from django.shortcuts import render,redirect
from .models import Geri_Donusum
from .forms import Geri_Donusum_Form

def geridonusumyeni(request):
    if request.method == "POST":
        forms = Geri_Donusum_Form(request.POST)
        if forms.is_valid():
            geri_don = forms.save(commit=False)
            geri_don.save()
            return redirect('gonderi_detay',pk = geri_don.pk)
    else:
        forms = Geri_Donusum_Form()
    return render(request,'GeriDonusum/yeni_geridon.html',{'form':forms})