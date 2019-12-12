from django.db import models

class tecrubeModel(models.Model):
    yatkinlik = models.CharField(max_length=200)
    kaynakekipman = models.CharField(max_length=200)
    uzmanlik = models.CharField(max_length=200)