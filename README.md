# proyecto-final-ekchy
Proyecto Final eKchý para presentación Instituto de Formación Técnica Superior N°18
# Anteproyecto
El anteproyecto está definido en este [documento] (https://docs.google.com/document/d/1RhiWL0GMZo7IJIyFtzYv9mnpVPzYhSBA/edit#heading=h.gjdgxs) [1]

# Mockups

En la carpeta [`mockups`](/mockups/) se encuentran los mockups de la app.

# Historias de Usuario

En el proyecto de Github [PP3 User Stories](https://github.com/users/JazminPineda/projects/1/views/1)
se puede visualizar como esta distribuido por etapas el proyecto, en cada etapa se tiene un proceso atomizado por historias de usuario en esta app..


# Comandos

`docker-compose run --rm proyectofinalekchy sh -c "python manage.py startapp user"`

## Ejecutar un script python en el contexto de django
1. `make docker-shell`
2. `python manage.py shell < dataextraction/lectura_excel.py`
3. `python manage.py shell < dataextraction/calculos.py`
