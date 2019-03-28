from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from seekerpet.mascotas import models
from seekerpet.mascotas import forms


class MascotasList(generic.ListView):
    template_name = 'mascotas/mascotas.html'
    model = models.Mascota

    def get_queryset(self):
        return models.Mascota.mostrar_mascotas_perdida()


class MascotaCreate(generic.CreateView):
    template_name = 'mascotas/formulario_mascota.html'
    form_class = forms.MascotaForm

    def get_success_url(self):
        return reverse_lazy('mascotas:listade_mascotas')

    def form_valid(self, form):
        # No olvidar registrar estados
        mascota = form.save(commit=False)
        mascota.propietario = self.request.user
        return super().form_valid(form)


class MascotaUpdate(generic.UpdateView):
    template_name = 'mascotas/formulario_mascota.html'
    form_class = forms.MascotaForm
    model = models.Mascota

    def get_success_url(self):
        return reverse_lazy('mascotas:listade_mascotas')

    def form_valid(self, form):
        mascota = form.save(commit=False)
        return super().form_valid(form)


class MascotaDetail(generic.DetailView):
    template_name = 'mascotas/detallede_mascota.html'
    model = models.Mascota

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['sigue_perdida'] = ctx.get('mascota').esta_perdida
        return ctx
