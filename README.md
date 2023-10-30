# ecommerce-plants
<p>Proyecto de backend desarrollado como parte de un bootcamp.</p>

<h1 align="center"> -----🪴 Plantalia  🪴----- </h1>

<h2>Instalación</h2>
<h3>1. Crea un entorno virtual:</h3>

```
python -m venv env

```
<h3>2. Activa el entorno virtual:</h3>

```
## en Unix:
source env/bin/activate
## en Windows:
env\Scripts\activate


```
<h3>3. Instala las dependencias del proyecto:</h3>

```
pip install -r requirements.txt

```
<h2> Configurar base de datos MySQL</h2>
<ul>
  <li>
    En la carpeta settings, crea un archvio con estos datos y sustituye:
    
    [client]
     database = <nameDataBase>
     user = <user>
     password = <password>
     default-character-set = utf8

  </li>
  <li>
    Ejecuta las migraciones 
    
    ```
    make makemigrations
    make migrate
    ```

  </li>
</ul>
