class Matrix:

    def __init__(self):
        self.row = 0
        self.column = 0
        self.matrix = []
	
    def putin(self):
        self.row = int(input("Rows: "))
        self.column = int(input("Column: "))
        print("Elements: ")
        self.matrix.append([[input() for a in range(self.column)] for b in range(self.row)])
        print()
    def printMatrix(self): 
        print("Matrix: ")
        for row in self.matrix:
            for matrix in row:
                print(matrix, end=' ')
                print()


example = Matrix()
example.putin()
example.printMatrix()
