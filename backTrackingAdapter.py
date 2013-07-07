from backtrackingAlgorithm import BacktrackingAlgorithm
class BackTrackingAdapter(object):
    """
    Posicion is a class that alow us to manage better every position in Sudoku

    """
    def __init__(self):
        self.backtrackingAlgorithm = BacktrackingAlgorithm()

    def solve(self, sudokuDic):
        sudokuMatrix = self.dict_to_list(sudokuDic)
        print("Received Sudoku")
        print(sudokuMatrix)
        resolvedSudokuMatrix  = self.backtrackingAlgorithm.solve(sudokuMatrix)
        print("Resolved Sudoku")
        print(resolvedSudokuMatrix)
        # converting to dictionary resolvedSudokuMatrix
        return self.list_to_dict(resolvedSudokuMatrix)

    #Funcion que devuelve una matriz apartir de un diccionario
    def dict_to_list(self, grid):
        """dict_to_list is a function to change the sudoku from a dictionary to a matrix
            It only works with 9 rows and 9 columns

        @param matrix: will contain the sudoku solved in a dictionary structure
        @return: a List of list with the sudoku numbers Zero instead of .
        """
        matrix = []
        for row in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']:
            matrix_row = []
            for column in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                matrix_row.append(0 if grid[row + column] == '.' else int(grid[row + column]))
            matrix.append(matrix_row)

        return matrix

    def list_to_dict(self, grid_as_list):
      row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
      column = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
      grid_as_dict = {}

      for j in range(9):
        for i in range(9):
            grid_as_dict[row[j] + column[i]] = '.' if grid_as_list[j][i] == 0 else str(grid_as_list[j][i])
      return grid_as_dict