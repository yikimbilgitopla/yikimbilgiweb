from django.db import models

class MaliyetModel(models.Model):
    makine = models.CharField(max_length=200)
    insan_gucu = models.CharField(max_length=200)
    