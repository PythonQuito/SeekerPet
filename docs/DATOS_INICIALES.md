# Carga de datos iniciales

Se puede realizar ingresando los datos en formato json en un archivo dentro la carpeta **fixtures**
Ejm: **mi_fixture.json**

```json
[
  {
    "model": "nombre_app.nombre_modelo",
    "pk": ##,
    "fields": {
      "nombre_campo": "valor_campo",
    }
  },
]
```

Una ves especificado el fixture se ejecuta:

`python manage.py loaddata mi_fixture`

El cual reescribirá los datos en el modelo.
