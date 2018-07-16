from django.db import models


# Create your models here.

class Posesion(models.Model):
    username = models.CharField(max_length=200)
    nameFigurita = models.CharField(max_length=10)
    contador = models.IntegerField(default=1)

class Ingreso(models.Model):
    username = models.CharField(max_length=200)
    monthDay = models.IntegerField(default=0)
    month = models.IntegerField(default=0)

class Peticion(models.Model):
    username = models.CharField(max_length=200)
    nameFigurita = models.CharField(max_length=200)
    isPide = models.BooleanField(default=True)


class Codigo(models.Model):
    codigo = models.CharField(max_length=200)
    isUsed= models.BooleanField(default=False)
