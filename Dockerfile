# Usa una imagen base oficial de Python
FROM python:3.10

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-dotenv

# Copia el resto de la aplicación
COPY . .

# Establece la variable de entorno para Flask
ENV FLASK_APP=app/main.py

# Expone el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
