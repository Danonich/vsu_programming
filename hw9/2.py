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

class Matrix2x2(Matrix):

    def check(self):
        if  self.row * self.column != 4:
            print("Matrix isn't 2x2")
        else:
            print("Matrix is 2x2")
            
            
example = Matrix2x2()
example.putin()
example.check()



