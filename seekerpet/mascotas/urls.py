from django.urls import path
from seekerpet.mascotas import views


app_name = 'mascotas'


urlpatterns = [
    path('', views.MascotasList.as_view(), name='listade_mascotas'),
    path('pet/create', views.MascotaCreate.as_view(), name='crear_mascota'),
    path('pet/<int:pk>/update', views.MascotaUpdate.as_view(), name='actualizar_mascota'),
    path('pet/<int:pk>/detail', views.MascotaDetail.as_view(), name='detalle_mascota'),

    path('pet/<int:pk>/info', views.info_mascota, name='info_mascota'),
    path('pet/<int:pk>/found', views.mascota_encontrada, name='mascota_encontrada'),
]