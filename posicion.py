class Posicion:
    """
    Posicion is a class that alow us to manage better every position in Sudoku

    """

    def __init__(self,maxfila,maxcol):
        self.maxfila = maxfila
        self.maxcol = maxcol
        self.fila = 0
        self.col = 0

    def setFila(self, fila):
        """setFila is going to asign the correct row value to any function

        :fila: is the number of row to execute a task
        :maxfila: is a constant that contains the number of total rows in Sudoku

        """
        if fila < 0:
            self.fila = 0
        elif fila >= self.maxfila:
            self.fila = -1
        else:
            self.fila = fila

    def setCol(self, col):
        """setCol is going to asign the correct column value to any function

        :col: is the number of column to execute a task
        :maxcol: is a constant that contains the number of total columns in Sudoku

        """
        if col < 0:
            self.col = 0
        elif col >= self.maxcol:
            self.col = -1
        else:
            self.col = col

    def getFila(self):
        return self.fila

    def getCol(self):
        return self.col

    def fin(self):
        return self.fila == -1 and self.col == -1

    def reset(self):
        self.fila = 0
        self.col = 0

    def sig(self):
        """sig function will give the next position in grid if fila and column are -1 if we are at the end of sudoku grid.
            This will control that position is out of the scope grids

       """

        if not self.fin():
            self.col += 1
            if self.col == self.maxcol:
                self.col = 0
                self.fila +=1
                if self.fila == self.maxfila:
                    self.fila = -1
                    self.col = -1

    def getPos(self):
        return [self.fila, self.col]
