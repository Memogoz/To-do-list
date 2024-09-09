# Utilizar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalar las dependencias del archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido de la aplicación Flask al directorio de trabajo
COPY . .

# Exponer el puerto en el que la aplicación correrá
EXPOSE 5000

# Comando para ejecutar Gunicorn en producción
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "nombre_del_paquete_o_archivo:app"]
