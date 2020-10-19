"""
Doc para correr los test con flask:
https://pypi.org/project/pytest-flask/
"""

from .backtracking import Backtracking
import pytest
SOLUCIONES = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]


def test_NReynas():
    bt = Backtracking(1)
    for i in range(1, 11):
        bt.limpiar()
        bt.N = i
        r = bt.resolver()
        assert r["cantSolucion"] == SOLUCIONES[i-1]
