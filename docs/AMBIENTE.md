# PREPARACIÓN DE AMBIENTE

## Prerequisitos

* Python 3
* Pip
* Virtualenv, Virtualenvwrapper, Venv (Opcional)

## Entorno virtual (Opcional)

### Instalación

* Virtualenv. https://virtualenv.pypa.io/en/latest/installation/
* Virtualenvwrapper. Virutalenv https://virtualenvwrapper.readthedocs.io/en/latest/install.html

### Preparación

* Virtualenv
  * virtualenv venv -p /path/a/python
  * source venv/bin/activate
* Virtualenvwrapper
  * mkvirtualenv venv -p /path/a/python
  * workon venv

## Proyecto

* Instalación dependencia
  * pip install -r requeriments.txt
* django-admin startproject seekerpet .
* python manage.py startapp mascotas seekerpet/mascotas
* python manage.py startapp seguridades seekerpet/seguridades