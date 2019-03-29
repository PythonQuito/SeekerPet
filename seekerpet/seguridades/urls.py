from django.urls import path
from seekerpet.seguridades import views


app_name = 'seguridades'


urlpatterns = [
    path('registro', views.RegistroView.as_view(),name='registro_usuario')
]