from django.contrib import admin
from seekerpet.seguridades import models


# python manage.py createsuperuser
admin.site.register(models.Perfil)
admin.site.register(models.Ciudad)
