from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from seekerpet.mascotas import managers


class Estado(models.Model):
    codigo = models.CharField(max_length=255, null=False, blank=True)
    nombre = models.CharField(max_length=255, null=False, blank=False)
    objects = managers.EstadoManager()

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return str(self.nombre)


class Mascota(models.Model):
    codigo = models.CharField(max_length=255, null=False, blank=True)
    nombre = models.CharField(max_length=255, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(null=False, blank=False)
    lugar_perdida = models.TextField(null=False, blank=False)
    fecha_perdida = models.DateField(null=False, blank=False)
    propietario = models.ForeignKey(User, null=False, blank=True, on_delete=models.CASCADE, related_name='mascotas')
    estado = models.ForeignKey(Estado, null=False, blank=True, on_delete=models.CASCADE, related_name='mascotas')

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

    def save(self, *args, **kwargs):
        if self.pk is None:
            code = '{}{}'.format(timezone.now().time(), self.nombre)
            self.codigo = hash(code.encode('utf-8'))
            self.estado = Estado.objects.perdida()
        return super().save(*args, **kwargs)

    @staticmethod
    def mostrar_mascotas_perdida():
        return Mascota.objects.filter(estado=Estado.objects.perdida()).order_by('-id')

    @property
    def esta_perdida(self):
        return self.estado == Estado.objects.perdida()

    def marcar_mascota_encontrada(self):
        self.estado = Estado.objects.encontrada()

    def informacionde_propietario(self):
        informacion = dict()
        informacion['propietario'] = self.propietario
        return informacion

    def __str__(self):
        return str(self.nombre)
