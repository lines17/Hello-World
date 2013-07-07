from backTrackingAdapter import BackTrackingAdapter
from backtrackingAlgorithm import BacktrackingAlgorithm
from posicion import Posicion

class Game:
    """
    Posicion is a class that alow us to manage better every position in Sudoku

    """
    def __init__(self):
        pass

    def main():
        '''sudoku=[[0,8,0,7,0,4,0,0,0],[9,0,4,0,0,0,6,0,8],[7,0,6,0,8,0,0,0,0],[0,0,0,2,0,8,0,6,5],[0,9,2,0,4,7,0,0,3],[0,0,0,0,0,0,0,0,0],[0,0,0,8,0,0,0,0,1],[4,6,5,0,2,0,0,8,9],[3,0,0,0,0,9,5,0,6]]
        '''

        sudoku =  {
                "A1":'.', "A2":'6', "A3":'7', "A4":'.', "A5":'4', "A6":'.', "A7":'.', "A8":'.', "A9":'2',
                "B1":'9', "B2":'.', "B3":'.', "B4":'7', "B5":'3', "B6":'.', "B7":'4', "B8":'5', "B9":'.',
                "C1":'4', "C2":'.', "C3":'5', "C4":'.', "C5":'.', "C6":'.', "C7":'.', "C8":'.', "C9":'.',
                "D1":'6', "D2":'.', "D3":'.', "D4":'.', "D5":'8', "D6":'.', "D7":'.', "D8":'.', "D9":'.',
                "E1":'.', "E2":'.', "E3":'.', "E4":'9', "E5":'.', "E6":'.', "E7":'3', "E8":'2', "E9":'.',
                "F1":'2', "F2":'8', "F3":'3', "F4":'5', "F5":'.', "F6":'.', "F7":'6', "F8":'4', "F9":'9',
                "G1":'.', "G2":'7', "G3":'.', "G4":'.', "G5":'.', "G6":'.', "G7":'.', "G8":'.', "G9":'3',
                "H1":'.', "H2":'.', "H3":'.', "H4":'6', "H5":'5', "H6":'7', "H7":'8', "H8":'.', "H9":'4',
                "I1":'.', "I2":'.', "I3":'6', "I4":'4', "I5":'2', "I6":'3', "I7":'5', "I8":'9', "I9":'7'
                }
        alg = BackTrackingAdapter()
        #alg.imprime (sudoku,[])
        resolvedSudokuAsDictionary = alg.solve(sudoku)
        print(resolvedSudokuAsDictionary)


    if __name__ == '__main__':
        main()