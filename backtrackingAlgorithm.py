#from sudoku.algorithm.Algorithm import Algorithm

# --------------clase Backtraking----------------
from posicion import Posicion

class BacktrackingAlgorithm(object):

    MAXLINEAS = 0
    MAXCOLS = 0
#Funcion que resuelve el sudoku
    def solve(self, sudoku):

        #sudoku = self.dict_to_list(grid)
        self.MAXLINEAS = len(sudoku)
        self.MAXCOLS = self.MAXLINEAS

        # Comenzamos en [0,0]
        pos = Posicion(self.MAXLINEAS,self.MAXCOLS)

        pilaActual = []
        pilaPosibles = []

        while not pos.fin():
            posibles = self.prueba(sudoku,pilaActual,pos.getFila(),pos.getCol())

            while posibles == []:
                if pos.fin():
                    # Hemos llegado al fin
                    solution = self.updateSudoku(sudoku,pilaActual)
                    #print (sudoku)
                    return solution

                pos.sig()
                posibles = self.prueba(sudoku,pilaActual,pos.getFila(),pos.getCol())

            if posibles == [-1]:
                # Backtracking
                estado = pilaActual.pop()
                while estado[0] != pilaPosibles[-1][0] or estado[1] != pilaPosibles[-1][1]:
                    estado = pilaActual.pop()
                # Ahora los ultimos estados de ambas tienen la misma posicion
                pilaActual.append(pilaPosibles.pop())
                # Ponemos la posicion correcta
                pos.setFila(pilaActual[-1][0])
                pos.setCol(pilaActual[-1][1])

            else:
                # Aqui tenemos unas posibles
                # Cojemos la primera y la apilamos en pilaActual, y el resto en pilaPosibles
                for posible in posibles[1:]:
                    pilaPosibles.append([pos.getFila(),pos.getCol(),posible])

                pilaActual.append([pos.getFila(),pos.getCol(),posibles[0]])


            pos.sig()

        resolvedSudoku = self.updateSudoku(sudoku,pilaActual)
        if not resolvedSudoku:
            raise InvalidSudokuException()
        else:
            return resolvedSudoku

    def existe(self, sudoku, num, linea, col):
        """existe is a function to verify if the number exists in row or column

        @param sudoku:
        @param encontrado:
        @param LINEAS:
        @param COLUMNAS:
        @return: a boolean if number exists in row or column could be True or False
        """
        encontrado = False
        for l in range(0,self.LINEAS):
            if sudoku[l][col] == num:
                encontrado = True

        for c in range(0,self.COLUMNAS):
            if sudoku[linea][c] == num:
                encontrado = True
        return encontrado


    def prueba(self, sudoku, asignadas, fila, col):
        """prueba is a function to verify if the number exists in row or column
            It could return three results:
            a) [] if position is busy
            b) a list of posible numbers
            c) [-1] it is imposible to solve

        @param sudoku:
        @param resultado:
        @param existe:

        @return: a list of posible values
        """
        if sudoku[fila][col] != 0:
            return []

        else:
            resultado = []

            # probamos todos los numeros posibles
            for n in range(1,self.MAXLINEAS+1):

                existe = False

                # barremos lineas
                for l in range(0,self.MAXLINEAS):
                    if sudoku[l][col] == n:
                        existe = True
                        break

                # barremos columnas
                for c in range(0,self.MAXCOLS):
                    if sudoku[fila][c] == n:
                        existe = True
                        break

                # barremos cuadrantes

                r1 = [0, 1, 2]
                r2 = [3, 4, 5]
                r3 = [6, 7, 8]
                if fila in r1:
                    rFilas = r1
                elif fila in r2:
                    rFilas = r2
                else:
                    rFilas = r3
                if col in r1:
                    rCols = r1
                elif col in r2:
                    rCols = r2
                else:
                    rCols = r3
                # verificamos en el cuadrante seleccionado
                for rr in rFilas:
                    for cc in rCols:
                        if sudoku[rr][cc] == n:
                            existe = True
                            break
                        for asig in asignadas:
                            if asig[0] == rr and asig[1] == cc and asig[2] == n:
                                existe = True
                                break





                # Buscamos en las posiciones asignadas
                for asig in asignadas:
                    if asig[0] == fila and asig[2] == n:
                        existe = True
                        break
                    if asig[1] == col and asig[2] == n:
                        existe = True
                        break

                    '''for rr in rFilas:
                        for cc in rCols:
                            if asig[0] == rr and asig[2] == n:
                                existe = True
                                break
                            if asig[1] == cc and asig[2] == n:
                                existe = True
                                break'''

                # add to asignadas
                if not existe:
                    resultado.append(n)
            # end for n
            if resultado == []:
                # Un callejon sin salida
                resultado = [-1]
            return resultado

    def updateSudoku(self, sudoku, asignadas):
        """imprime is a function to display and asign the sudoku solved

        @param dict_result: will contain the sudoku solved in a dictionary structure
        @param sudoku:
        @param asignadas:

        @return: a dictionary with the sudoku solved where the Key is the Row and column of sudokugame and Value is the number asigned to solve sudoku
        """
        for fila in range(0,len(sudoku)):
            for columna in range(0,len(sudoku)):
                if sudoku[fila][columna] == 0:
                    for a in asignadas:
                        if a[0] == fila and a[1] == columna:
                            sudoku[fila][columna] = a[2]
        return sudoku