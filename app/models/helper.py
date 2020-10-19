"""
    Metodos de utileria para insertar, consultar y eliminar  en la tabla NReynas
"""
from app.models.models import NReynas
from app.models.db import session
import json

def insertar_solucion(Bt):
    """
        Inserta la solucion previamente computada
    :return: void

    """
    n_reyna = NReynas(N=Bt.N, Soluciones=json.dumps(Bt.R), N_soluciones=len(Bt.R))
    session.add(n_reyna)

    session.commit()


def obtener_solucion(cantidad:int):
    """
    Metodo encargado de obtener las soluciones de la base de datos dependiente de la 'cantidad' de reynas
    :param cantidad: Reynas a considerar
    :return:dict
    """

    soluciones = session.query(NReynas).filter_by(N=cantidad).first()
    if soluciones is None:
        msg = 'No existe registro previo para ('+str(cantidad)+'). '
        msg += 'Consulte http://127.0.0.1:500/resolver/'+str(cantidad)
        return {'msg': msg}
    out = {"N": soluciones.N, "cantSolucion": soluciones.N_soluciones, "soluciones": soluciones.Soluciones}

    return out


def eliminar_solucion_anterior(N:int):
    """
    Elimina solucion existente en la base de datos
    :param N:
    :return: dict
    """
    res = {'msg': 'Nada que hacer', 'code': 200}
    resgistro = session.query(NReynas).filter_by(N=N).first()
    if resgistro is not None:
        session.delete(resgistro)
        session.commit()
        res['msg'] = 'Registro eliminado'

    return res


