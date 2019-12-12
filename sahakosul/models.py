from django.db import models

class SahaModel(models.Model):
    sahaGuvenlik = models.CharField(max_length=200)
