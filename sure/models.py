from django.db import models

class sureModel(models.Model):
    sahaHazirligi = models.CharField(max_length=200)
    yikimSureci = models.CharField(max_length=200)