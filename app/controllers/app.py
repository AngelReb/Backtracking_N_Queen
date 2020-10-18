from flask import Flask
from flask import url_for
from flask import escape
from flask import request
from flask import jsonify

from app.models.db import init_db
from app.models.models import NReynas
from app.models.Solucion import Backtracking

app = Flask(__name__)

@app.route('/')
def index():
    return "index file :)"


@app.route('/solucion', methods=['GET'])
@app.route('/solucion/<int:cantidad>', methods=['GET'])
def solucion(cantidad=0):

    #init_db()
    sr = Backtracking(cantidad)

    solucion = sr.resolver()

    #print(solucion)

    return jsonify(solucion)

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


with app.test_request_context():
    print(url_for('index'))
    print(url_for('solucion'))
    print(url_for('profile', username='John Doe'))
    assert request.method == 'GET'

if __name__ == "__main__":
    app.run()

    print("Ejecutnado servicios")