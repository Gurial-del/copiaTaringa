# 1. BASE: Usamos una imagen oficial de Python (como comprar una compu con Linux y Python ya instalado)
# "slim" significa que es una versión ligera para que descargue rápido
FROM python:3.12-slim
# la siguiente linea le dice a python que no se guarde nada, que lo imprima
ENV PYTHONUNBUFFERED=1 

# 2. DIRECTORIO: Creamos una carpeta de trabajo dentro de la caja
WORKDIR /app

# 3. DEPENDENCIAS: Copiamos la lista de ingredientes y los instalamos
# Copiamos primero solo el requirements para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. CÓDIGO: Copiamos todo el resto de tu código a la caja
COPY . .

# 5. PUERTO: Le decimos al mundo que esta caja escucha en el puerto 8000
EXPOSE 8000

# 6. ARRANQUE: El comando que se ejecuta cuando la caja se enciende
# OJO: Usamos 0.0.0.0:8000 para que sea accesible desde fuera del contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]