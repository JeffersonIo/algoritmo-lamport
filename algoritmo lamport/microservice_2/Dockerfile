# Usamos una imagen base de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos los archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Exponemos el puerto en el que correrá Flask
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
