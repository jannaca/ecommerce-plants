# Utiliza una imagen base que contenga Python y un sistema operativo compatible.
FROM python:3.9

# Establece variables de entorno para Django
ENV DJANGO_SETTINGS_MODULE=myproject.settings
ENV DJANGO_SECRET_KEY=mysecretkey

# Crea y establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el código fuente de tu proyecto a la imagen
COPY . /app

# Instala las dependencias de tu proyecto
RUN pip install -r requirements.txt

# Exponer el puerto que tu aplicación Django utiliza (por defecto 8000)
EXPOSE 8000

# Iniciar la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
