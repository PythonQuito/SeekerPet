from django.db import models
from seekerpet.mascotas import models as modelosde_mascotas

PERDIDA = '001'
ENCONTRADA = '002'
SINRESULTADO = '003'

class EstadoManager(models.Manager):

    def perdida(self):
        return modelosde_mascotas.Estado.objects.filter(codigo=PERDIDA).first()
    
    def encontrada(self):
        return modelosde_mascotas.Estado.objects.filter(codigo=ENCONTRADA).first()
    
    def sin_resultado(self):
        return modelosde_mascotas.Estado.objects.filter(codigo=SINRESULTADO).first()