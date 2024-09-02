# Info de la materia: ST0263-242 Tópicos Especiales en Telemática.

# Estudiantes

| [<img src="https://avatars.githubusercontent.com/u/81777898?s=400&u=2eeba9c363f9c474c7fb419ef36562e2d2b6b866&v=4" width=115><br><sub>MURICIO DAVID CORREA HERNÁNDEZ.<br>Correo: mdcorreah@eafit.edu.co</sub>](https://github.com/MauricioDCH) | [<img src="https://avatars.githubusercontent.com/u/69641241?v=4" width=115><br><sub>SALOMÓN VÉLEZ PÉREZ <br>Correo: svelezp10@eafit.edu.co</sub>](https://github.com/svelezp) |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------: |
#
# Profesor: Edwin Nelson Montoya Múnera, emontoya@eafit.edu.co

# Nombre del proyecto: Arquitectura P2P y Comunicación entre procesos mediante API REST, RPC y MOM.
#
# 1. Breve descripción de la actividad

Se  busca desarrollar un sistema P2P descentralizado en anillo, en el que los nodos puedan comunicarse entre ellos y con el que se simule la transferencia de archivos entre nodos.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Creacion de nodos, asignacion de las respectiva finger table de cada nodo, conformacion de un servidos encargado de registrar los nodos del sistema con sus respectivas IDs e IPs. 


## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Despliegue en contenerizacion con docker.

# 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

![alt text](Application/Images/Arquitectura_Inicial_P2P.jpg)

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

El lenguaje usado ha sido python, con archivos .proto para la comunicacion con grpc. 

Las librerias usadas son las siguientes:

- blinker
- certifi
- charset-normalizer
- click
- Flask
- grpcio
- grpcio-tools
- idna
- itsdangerous
- Jinja2
- MarkupSafe
- pip
- protobuf==5.27.2
- requests
- setuptools
- urllib3
- Werkzeug
- ujson
- pandas

## Como se compila y ejecuta.
Correr en una terminal el codigo del server, el cual actua como un nodo de la red, y en otra terminal correr el codigo de cliente, desde donde se hacen las peticiones al nodo servidor.

## Detalles del desarrollo.
El sistema se hizo usando gRPC como tecnologia de conexion entre los nodos. Cada nodo tiene la capacidad de actuar como servidor y como cliente dependiendo de la necesidad. Si un nodo actua como servidor de una peticion, pero debe re direccionar la peticion a otro nodo, este nodo seria ahora un cliente.
## Detalles técnicos

## Descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
Dentro de la clase serve, se configura el puerto en el que se iniciara el nodo servidos
## Opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)

## 
## Opcionalmente - si quiere mostrar resultados o pantallazos 



# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

En la ejecucion, las librerias usadas son las mismas que las mencionadas anteriormente en el desarrollo, debido a que no se logro implementar el despliegue usando docker.



# IP o nombres de dominio en nube o en la máquina servidor.

## Descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
En el codigo, donde se habia configurado algunas variables como local host, se remplaza con la ip del nodo al que se quiere conectar.

## Como se lanza el servidor.
 Cada maquina virtual puede actuar como servidor o cliente, para actuar como servidor debe correrse el archvi de server.py en la maquina que se desee, y asi esta entrara a la red.

## Una mini guia de como un usuario utilizaría el software o la aplicación

1. Inicializar las maquinas virtuales de aws
2. Clonar el repositorio en las maquinas virtuales y cambiar las variables necesarias, como direcciones IPs.
3. Inicializar el nodo 0, el cual tendra la tabla que contendra el ID y la direccion IP de cada nodo
4. Inicializar el resto de nodos para llenar la tabla del nodo 0.
5. Hacer las peticiones que se deseen, como descarga o carga de archivos.

## Opcionalmente - si quiere mostrar resultados o pantallazos 

# 5. Otra información que considere relevante para esta actividad.

# Referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## sitio1-url 
## sitio2-url
## url de donde tomo info para desarrollar este proyecto
