# Problema de las N reynas

## Requerimientos
Tener Docker y Docker compose instalados

## Para levantar el proyecto, ejecute los siguientes comandos
> docker-compose build 
>
> docker-compose up
 
## Algunos puntos a tomar en cuenta para el problema de Bracktraking

* Determina todas las posibles soluciones dado N donde N ≥ 8 (en 10 mins sobre una laptop). 
    Bonus para N donde N es el tamaño del tablero / Num de reynas

* Se iterar sobre N y almacenar las soluciones en un postgres utulizando SQLAlchemy
    
* UnitTest que al menos verifica el numero de soluciones dado N

* Solución Dockerizada, Se puede correr las pruebas sin depender de configurar el ambiente de la solución
    
* CI con Travis


## Consumir el servicio 

### Calcular solucion al problemas de las N-Reynas
> http://127.0.0.1:5000/resolver/4
>
> http://127.0.0.1:5000/resolver/8

### Obtener solucion desde la base de datos
> http://127.0.0.1:5000/solucion_guardada/8

### Eliminar registro previo en la base de datos dado 'N'
> http://127.0.0.1:5000/delete/8


