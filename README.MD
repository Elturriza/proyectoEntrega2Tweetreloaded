# TwitterReloaded

## Description

Este proyecto simula la funcion de tweets e hilos de twitter

## Requirements

Se necesitara instalar python3 y docker, todo eso viene en el archivo requirements.txt

## Installation
Simplemente es correr los comandos de docker siguientes:

## Docker
1. construi la imagen:
docker-compose up --build
Esto ejecutara docker-compose.yml y el dockerfile que instalara lo necesario para crear un contenedor con la aplicacion y MySql

2. Ejecutar el contenedor:
Se iniciara el localhost en automatico, se debe tener libre el puerto 80 para la aplicación y el 3306 que es el predeterminado de MySql

3. Acceder a la aplicación en el navegador:
http://localhost:80


4. Detener el contenedor:
docker stop CONTAINER_ID

## Observaciones
Puede aparecer un error de la base de datos que no existen las tablas a pesar que se tiene incluido los archivos.sql que crean las tablas y la base de datos para ello se pueden correr lso siguientes comandos:

1. docker-compose exec db mysql -uroot -proot tweetreloaded Esto es para acceder a MySql en el cmd line

2. Correr los querys siguientes:

CREATE DATABASE IF NOT EXISTS tweetreloaded;
USE tweetreloaded;

CREATE TABLE tweets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    person VARCHAR(255),
    content VARCHAR(255)
);

CREATE TABLE replies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tweet_id INT,
    content TEXT,
    person VARCHAR(255),
    FOREIGN KEY (tweet_id) REFERENCES tweets(id)
);

3. En caso que el error sea que no se pueda acceder al localhost:3306 se puede acceder a windows+r escribir services.msc y detener MySql, esto detendra MySql de manera local y permitira correr en docker el puerto.

## SOLID Practices

1. SRP.- Esto lo cumplo al tener la clase service y dbcon donde service se encarga de las operaciones de negocio y dbcon la lógica de acceso de datos y las llamadas a la base de datos.

2. OCP.- Se cumple al no tener que modificar las funcionalidades ya existentes pero de necesitar agregar algo no habria problemas para extender la clase.

3. LSP.- Lo cumplo al hacer que Reply herede la clase Tweet ya que contienen atributos similares

4. ISP.- Al dividir las funcionalidades en tweet, insert_reply y get_recent_tweets.

5. DIP.- Se cumple al momento en que service depende de la clase dbconn por medio de la instancia.

## Design Patterns
1. Factory.- Lo cumplo al crear los objetos en service de tweet y reply
2. Strategy.- Lo cumplo cuando llamo a la funcion create something para decidir si es un reply o tweet.
3. Repository.- Lo cumplo al separar en layers la aplicacion 