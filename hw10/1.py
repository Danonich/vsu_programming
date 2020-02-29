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
            self.matrix.append([int(input()) for b in range(self.row)])
        print()
    
    def __str__(self): 
        print("Matrix: ")
        f = ' '
        for x in self.matrix:
            f += '\n'
            for m in x:
                f += f'{m}  '
        return f

    def set_elem(self, s, c, value):
       self.check(value)
       self.matrix[s][c] = value
    
    def check(self, value):
      if not isinstance(self, int):
          print('Значение должно быть числом!!!')

class Matrix2x2(Matrix):

    def determinant(self):
        if  self.row * self.column != 4:
            print("Matrix isn't 2x2")
        else:
            arg2 = 0
            arg1 = 0   
            for a in range(self.column):
                for b in range(self.row):
                    arg1 = self.matrix[0][0] * self.matrix[self.row - 1][self.column - 1]
                    arg2 = self.matrix[0][self.column - 1] * self.matrix[self.row - 1][0]
            print("Determinant 2x2:", arg1 - arg2)                    
            
example = Matrix2x2()
example.putin()
x=9
example.set_elem(1,1,x)
example.determinant()
