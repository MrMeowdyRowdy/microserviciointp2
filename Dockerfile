# Imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir flask flask-sqlalchemy

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 5002

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
