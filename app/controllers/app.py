from flask import Flask
from flask import url_for
from flask import escape
from flask import request
from flask import jsonify

from app.models.db import DATABASE_URI
from app.models.models import Base, engine, session, NReynas, create_db
from app.models.Solucion import Backtracking

app = Flask(__name__)

create_db()

@app.route('/')
def index():
    Base.metadata.create_all(engine)
    return "index file :)"


@app.route('/resolver', methods=['GET'])
@app.route('/resolver/<int:cantidad>', methods=['GET'])
def solucion(cantidad=0):
    #Creamos instancia de la clase encargada de la logica
    back_t = Backtracking(cantidad)

    #Eliminamos registro previo
    res = Backtracking.eliminar_solucion_anterior(cantidad)

    #Obtenemos la solucion al tablero NxN
    solucion = back_t.resolver()

    #Se inserta la solucion
    back_t.insertar_solucion()

    #Regresamos respuesta
    return jsonify(solucion)

@app.route('/solucion_guardada/', methods=['GET'])
@app.route('/solucion_guardada/<int:cantidad>', methods=['GET'])
def obtener(cantidad=0):
    res = Backtracking.obtener_solucion(cantidad)
    return jsonify(res)

@app.route('/delete/', methods=['GET'])
@app.route('/delete/<int:cantidad>', methods=['GET'])
def eliminar(cantidad=0):
    res = Backtracking.eliminar_solucion_anterior(cantidad)
    return jsonify(res)


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'msg': 'Pagina no encontrada', 'code': 404})


with app.test_request_context():
    print(url_for('index'))
    print(url_for('solucion'))
    print(url_for('obtener'))


