import uuid
from django.db import models

# Create your models here.

class Receta(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    dificultad = models.PositiveSmallIntegerField()
    imagen = models.ImageField(upload_to="recetas", null=True)
 
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.dificultad)