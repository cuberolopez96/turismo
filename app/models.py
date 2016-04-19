from __future__ import unicode_literals

from django.db import models

class ComunidadAutonoma(models.Model):
    nombre=models.CharField(max_length=250)
    def __unicode__(self):
        return self.nombre
class Provincia(models.Model):
    nombre=models.CharField(max_length=250)
    idCCAA=models.ForeignKey(ComunidadAutonoma)
    def __unicode__(self):
        return self.nombre
class rutas(models.Model):
    idProvincia = models.ForeignKey(Provincia)
    nombre=models.CharField(max_length=250)
    enlaceRuta = models.CharField(max_length=250)
    def __unicode__(self):
        return self.nombre