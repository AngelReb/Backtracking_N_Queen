
from flask import jsonify
import json
class Backtracking:

    def __init__(self, n):
        """

        :param n: Cantidad de reynas
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
            'solucion' Es un array con las posicion de las reynas,
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
        f = open('test.txt', 'w')
        f.write(json.dumps(out))
        f.close()

        return out
    def backtracking(self,reynas, columna):
        #Condicion de termino
        #if columna_actual >= self.N:
        #   return solucion

        #Iteramos los renglones de cada columna
        for renglon in range(0, self.N):
            #para este renglon es una posicion valida?
            if self.validarRenglon(reynas, columna, renglon):
                #Colocamos la reyna en la columna y renglon
                reynas[columna] = renglon
                #if '-' not in reynas:

                if columna == self.N-1:
                    #terminamos de iterar, se verifica si guardar o no solucion
                    self.R.append(reynas)
                else:
                    self.backtracking(reynas.copy(), columna+1 )

    def validarRenglon(self, reynas, columna, renglon):
        if renglon in reynas:
            #Ya existe reyna en el mismo renglon
            return False
        for col in range(0, columna):
            #Obtenemos el actual renglon de la reyna que estamos iterando
            renglon_reyna_ite = reynas[col]
            columna_reyna_ite = col

            #Valor de la casilla para ambas diagonales de la reyna iterada
            casilla_reyna_ite_ds = renglon_reyna_ite + columna_reyna_ite
            casilla_reyna_ite_di = renglon_reyna_ite - columna_reyna_ite

            diagonal_superior = renglon + columna
            diagonal_inferior = renglon - columna
            #Verificamos si existe en la diagonal superior: RENGLON+COL
            if casilla_reyna_ite_ds == diagonal_superior:
                return False

            #Verificamos si existe en la diagonal inferior: RENGLON-COL
            if casilla_reyna_ite_di == diagonal_inferior:
                return False

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
