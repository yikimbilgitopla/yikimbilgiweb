from django.db import models

class yapiOzellikModel(models.Model):
    Yukseklik = models.CharField(max_length=200)
    Tip = models.CharField(max_length=200)
    Stabilite = models.CharField(max_length=200)
    yikimSeviyesi = models.CharField(max_length=200)
    yapininKullanimi = models.CharField(max_length=200)
