# ecommerce-plants
<p>Proyecto de backend desarrollado como parte de un bootcamp.</p>

<h1 align="center"> -----🪴 Plantalia  🪴----- </h1>

<h2>Requisitos previos</h2>
<p>Antes de comenzar, asegurate de tener instalado Makefile en tu sistema.</p>
<p class="text-center">o</p>
<p>Usa la ruta larga para los comandos tal como:</p>

```
python manage.py runserver --settings=settings.local
```

<h2>Instalación</h2>

<h3>1. Crea un entorno virtual:</h3>

```
python -m venv env
```
<h3>2. Activa el entorno virtual:</h3>

```
# en Unix:
source env/bin/activate
# en Windows:
env\Scripts\activate
```
<h3>3. Instala las dependencias del proyecto:</h3>

```
pip install -r requirements.txt
```
<h2> Configurar base de datos MySQL</h2>
<ul>
  <li>
    En la carpeta settings, crea un archvio llamado "my.cnf" con estos datos y sustituye:
    
    [client]
     database = <nameDataBase>
     user = <user>
     password = <password>
     default-character-set = utf8

  </li>
  <li>
    Ejecuta las migraciones 
    
    make makemigrations
    make migrate

  </li>

  <li>
    Cargar datos iniciales en la base de datos
    
    make loaddata

  </li>
  <li>
    Inicia el servidor:

    make runserver

  </li>
  <li>
    Crear un super usuario y acceder al admin

    make superuser

  </li>

  <li>
    Para ejecutar pruebas en el proyecto

    make test

  </li>
</ul>

<h2>---Live DEMO ---</h2>

http://jannaca.pythonanywhere.com/

