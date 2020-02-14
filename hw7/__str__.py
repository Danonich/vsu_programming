class Matrix:

    def __init__(self):
        self.row = 0
        self.column = 0
        self.matrix = []
	
    def putin(self):
        self.row = int(input("Rows: "))
        self.column = int(input("Column: "))
        print("Elements: ")
        for a in range(self.column):
            self.matrix.append([input() for b in range(self.row)])
        print()
    def __str__(self): 
        print("Matrix: ")
        for x in self.matrix:
            print(' '.join(str(m) for m in x))




example = Matrix()
example.putin()
example.__str__()
