
from flask import jsonify
import json
class Backtracking:

    def __init__(self, n, r=[]):
        """

        :param n: integer Cantidad de reynas
        :param r: list  Lista donde se guardaran las soluciones, cada solucion es una lista con posicion de las reynas
        """

        self.N = n
        self.R = []

    def resolver(self):
        """
        Metodo encargado de resolver el problema dado el atributo 'N' de reynas

        Descripcion de como se guardan los datos
        ---------
            Diccionario con elementos: 'cantidad' y 'solucion'.
            'cantidad' Numero de soluciones referente a las reynas solicitadas para la solucion
            'solucion' Es una list<list:int> con las posicion de las reynas,
                      Donde cada indice del array hace referencia al numero de columna
                      y su valor al renglon

            Ejemplo: tablero nxn
            dict = {'cantidad': 4, 'soluciones': [[1,3,0,2], [2,0,3,1]]}
            \n
            [1,3,0,2]
            R/C   0 1 2 3    \n
            0   [ - - Q - ]  \n
            1   [ Q - - - ]  \n
            2   [ - - - Q ]  \n
            3   [ -Q- - - ]

            [2,0,3,1]
            R/C   0 1 2 3    \n
            0   [ - Q - - ]  \n
            1   [ - - - Q ]  \n
            2   [ Q - - - ]  \n
            3   [ - - Q - ]
        :return: dict \n
        """
        #Creamos un arreglo donde '-' especifica que no hay ninguna reyna colocada
        reynas_iniciales = ['-'] * self.N
        columna_inicial = 0
        self.backtracking(reynas_iniciales, columna_inicial)

        out = {"N": self.N, "cantSolucion": len(self.R), "soluciones":  self.R}

        return out

    def backtracking(self, reynas, columna):
        """
        Metodo recursivo que resuelve el problema de las N-reynas.
        Se intentara colocar una reyna para la columna actual

        :param reynas: lista de reynas por cada solucion. Lista de 'self.N' elementos < 0 o de caracteres
        :param columna: columna actual
        :return: void
        """
        #Condicion de termino, superamos la cantidad de columnas para el tablero NxN
        if columna == self.N:
           return

        #Iteramos los renglones de cada columna
        for renglon in range(0, self.N):
            #para este renglon es una posicion valida?
            if self.validarRenglon(reynas, columna, renglon):
                #Colocamos la reyna en la columna y renglon
                reynas[columna] = renglon

                if columna == self.N-1:
                    #Se llego a una ultima columna donde la reyna es valida colocar, guardamos solucion
                    self.R.append(reynas)
                else:
                    #Aun faltan columnas por recorrer
                    self.backtracking(reynas.copy(), columna+1)
            #Sino hay renglon valido para la reyna actual se descarta solucion
            elif renglon == self.N-1 and reynas[columna] == '-':
                return

    def validarRenglon(self, reynas, columna, renglon):
        """
        Validamos que dada la posicion  columna y renglon no existe reyna que sea atacada.
        Regresa:
            True si es seguro colocar reyna

            False si alguna reyna es atacada
        :param reynas: list
        :param columna: int Columna actual
        :param renglon: int Renglon actual
        :return: bool True o False dependiendo si es valido colocar reyna
        """
        if renglon in reynas:
            #Ya existe reyna en el mismo renglon
            return False

        for col in range(0, columna):
            #Obtenemos el actual renglon y columna de la reyna que estamos iterando
            renglon_reyna_ite = reynas[col]
            columna_reyna_ite = col

            #Valor de la casilla para ambas diagonales de la reyna iterada
            casilla_reyna_ite_ds = renglon_reyna_ite + columna_reyna_ite
            casilla_reyna_ite_di = renglon_reyna_ite - columna_reyna_ite

            #Valor de la casilla para la reyna que estamos intentando colocar
            diagonal_superior = renglon + columna
            diagonal_inferior = renglon - columna

            #Verificamos si existe en la diagonal superior: RENGLON+COL
            if casilla_reyna_ite_ds == diagonal_superior:
                return False

            #Verificamos si existe en la diagonal inferior: RENGLON-COL
            if casilla_reyna_ite_di == diagonal_inferior:
                return False
        #Si ninguna reyna ya colocada es atacada por la nueva
        return True


    def insertarSolucion(self):
        """
            Inserta la solucion previamente computada
        :return: void

        """
        pass
    def obtenerSolucion(self, cantidad:int, texto:str ):
        """
        Metodo encargado de obtener las soluciones de la base de datos dependiente de la 'cantidad' de reynas
        :param cantidad: Reynas a considerar
        :return:json
        """
        pass
    def print_solucion(self):
        """
         Imprime la solucion al problema dada una 'cantidad' de reynas en consola

         """
        out = {"cantidad": self.N, "solucion": {}}

        return out
