from django.db import models
from django.contrib.auth.models import User


class Ciudad(models.Model):
    codigo = models.CharField(max_length=255, null=False, blank=True)
    nombre = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
    
    def __str__(self):
        return str(self.nombre)


class Perfil(models.Model):
    telefono = models.CharField(max_length=13, null=False, blank=False)
    direccion = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, null=False, blank=True, on_delete=models.CASCADE, related_name='perfil')
    ciudad = models.ForeignKey(Ciudad, null=False, blank=False, on_delete=models.CASCADE, related_name='perfiles')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    @staticmethod
    def crear_perfil(user, telefono, direccion, ciudad, **kwargs):
        perfil = Perfil(
            user=user, telefono=telefono, direccion=direccion, ciudad=ciudad
        )
        
        return perfil

    def __str__(self):
        return str(self.user)