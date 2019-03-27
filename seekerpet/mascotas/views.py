from django.shortcuts import render
from django.views import generic
from seekerpet.mascotas import models


class MascotasList(generic.ListView):
    template_name = 'mascotas/mascotas.html'
    model = models.Mascota

    def get_queryset(self):
        return models.Mascota.mostrar_mascotas_perdida()
