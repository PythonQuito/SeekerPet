from django.db import transaction
from django.urls import reverse_lazy
from django.views import generic
from seekerpet.seguridades import forms
from seekerpet.seguridades import models


class RegistroView(generic.CreateView):

    template_name = 'registration/registro.html'
    form_class = forms.RegistroForm

    def get_success_url(self):
        return reverse_lazy('login')

    def form_valid(self, form):
        with transaction.atomic():
            user = form.save(commit=False)
            user.set_password(self.request.POST.get('password'))
            user.save()

            perfil = models.Perfil.crear_perfil(
                user=user, **form.cleaned_data
            )
            perfil.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)