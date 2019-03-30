from django import forms
from seekerpet.mascotas import models


class MascotaForm(forms.ModelForm):

    class Meta:
        model = models.Mascota
        exclude = ['codigo', 'propietario', 'estado']
