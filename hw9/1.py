class Matrix:

    def __init__(self, matrix):
        self.row = None
        self.column = None
        self.matrix = matrix	
    def __str__(self): 
        print("Matrix: ")
        f = ''
        for x in self.matrix:
            f += '\n'
            for m in x:
                f += f'{m}  '
        return f


b = [[1,2,3] , [4,5,6]]
example = Matrix(b)
print(example)
