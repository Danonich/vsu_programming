class Matrix:

    def __init__(self):
        self.string = None
        self.row = None
        self.matrix = []
	
    def putin(self):
        self.string = int(input("Strings: "))
        self.row = int(input("Rows: "))
        print("Elements: ")
        self.matrix = [[input() for j in range(self.row)] for i in range(self.string)]
        print()
    def printMatrix(self): 
        print("Matrix: ")
        matrix = self.matrix
        for i in range(len(matrix)):
            print(matrix[i])


example = Matrix()
example.putin()
example.printMatrix()
