# **Steps for a Perfect Execution**

## Laura Fernández del Moral García Consuegra Group C2

## Installation

1. To locally install the package, just run

```
pip install .
```

## Execution
SERVIDOR
- Instalar docker en el servidor.
- Editar fichero "/etc/hosts" y asignar alias a la ip publica el nombre "kafka". 		ejemplo   "181.20.30.5  kafka".
- Copiar el fichero docker-compose.yam
- Ejecutar "docker-compose up -d" con permisos para crear Docker.
- Ejecutar en la carpeta raiz del repositorio "remotetypes prueba5_topic kafka", donde "prueba5_topic" se puede elejir cualquier TOPIC, en el cliente tendría que ser el mismo.
CLIENTE.
- En la carpeta raiz del repositorio ejecutar "remotetypes-client prueba5_topic ip_server", el TOPIC tiene que ser el mismo que el servidor.
CLIENTE-TEST
- En la carpeta raíz del repositorio ejecutar "remotetypes-test prueba5_topic ip_server", el TOPIC tiene que ser el mismo que el servidor Es un cliente sencillo que lee datos el fichero “./daots/source.txt” y crea un fichero con la información de los datos almacenados en el servidor.
### For the test
```
pytest
```
