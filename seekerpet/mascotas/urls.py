from django.urls import path
from seekerpet.mascotas import views


app_name = 'mascotas'


urlpatterns = [
    path('', views.MascotasList.as_view(), name='listade_mascotas'),
]