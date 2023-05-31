FROM python:3.10.11-slim

WORKDIR /app

# Copiar los archivos de la aplicación
COPY . /app
COPY requirements.txt /app
COPY app.py .
COPY dbcon.py .
COPY service.py .
COPY templates /app/templates

# Instalar las dependencias de la aplicación
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]
