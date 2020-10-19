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


@app.route('/solucion', methods=['GET'])
@app.route('/solucion/<int:cantidad>', methods=['GET'])
def solucion(cantidad=0):

    sr = Backtracking(cantidad)

    solucion = sr.resolver()
    sr.insertarSolucion()

    #print(solucion)
    session.commit()
    return jsonify(solucion)

@app.route('/obtener/', methods=['GET'])
@app.route('/obtener/<int:cantidad>', methods=['GET'])
def obtener(cantidad=0):
    res = Backtracking.obtenerSolucion(cantidad)
    return jsonify(res)

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'msg': 'Pagina no encontrada', 'code': 404})


with app.test_request_context():
    print(url_for('index'))
    print(url_for('solucion'))
    print(url_for('obtener'))


