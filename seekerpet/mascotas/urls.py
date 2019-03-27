from django.urls import path
from seekerpet.mascotas import views


app_name = 'mascotas'


urlpatterns = [
    path('', views.MascotasList.as_view(), name='listade_mascotas'),
    path('pet/create', views.MascotaCreate.as_view(), name='crear_mascota'),
    path('pet/<int:pk>/update', views.MascotaUpdate.as_view(), name='actualizar_mascota'),
]