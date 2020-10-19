#Cuenca-Coding_challenge Luis Angel Reyes Bautista

##Requerimientos
Tener Docker y Docker compose instalados

##Para levantar el proyecto, ejecute los siguientes comandos
> docker-compose build 
>
> docker-compose up
 

##Consumir el servicio 

###Calcular solucion al problemas de las N-Reynas
> http://127.0.0.1:5000/resolver/4
>
> http://127.0.0.1:5000/resolver/8

###Obtener solucion desde la base de datos
> http://127.0.0.1:5000/solucion_guardada/8

###Eliminar registro previo en la base de datos dado 'N'
> http://127.0.0.1:5000/delete/8


##To-dos 
1- *check*

    Determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop). 
    Bonus points for a higher N where N is the size of the board / number of queens
2- *check*

    Iterate over N and store the solutions in postgres using SQLAlchemy
    
3- *check*
    
    Write basic tests that at least verify the number of solutions for a given N match what's online. I recommend using pytest
    
4- *check*

    Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup (including running a postgres instance in docker-compose)
    
5- *check*

    Setup Travis CI (or similar) for your public GitHub repo to run the tests automatically

##Algunos link de referencia

###Doc oficial de Docker y Docker compose
https://docs.docker.com/

https://docs.docker.com/compose

###Imagen python
https://hub.docker.com/_/python

###Imagen postgres
https://hub.docker.com/_/postgres

####Docker compose para python y postgres
######(Omitir que es para django xD)
https://docs.docker.com/compose/django/

###SQLAlchemy Crear sesiones y conectar con la base de datos
https://docs.sqlalchemy.org/en/13/orm/tutorial.html

http://zetcode.com/db/sqlalchemy/

###Env Configuracion de env.files en docker compose
https://docs.docker.com/compose/compose-file/#env_file

###Flask Doc oficial
https://flask.palletsprojects.com/en/1.1.x/ 

###Pytest con flask
https://pypi.org/project/pytest-flask/

###Travis
https://docs.travis-ci.com/

###Configuracion de redes IPV4:
https://docs.docker.com/compose/compose-file/compose-file-v2/#ipv4_address-ipv6_address
