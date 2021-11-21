class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def print(self):
        print(self.matrix)

    # Add matrices

    def __add__(self, other):

        try:
            rows_m1 = len(self.matrix)
            rows_m2 = len(other.matrix)
            cols_m1 = [len(self.matrix[0])]
            cols_m2 = [len(other.matrix[0])]

            if rows_m1 == rows_m2:
                if cols_m1 == cols_m2:
                    return Matrix([[col_m1 + col_m2 for (col_m1, col_m2) in zip(row_m1, row_m2)] for (row_m1, row_m2) in
                                   zip(self.matrix, other.matrix)])
                else:
                    raise ValueError("Number of rows is different")
            else:
                ValueError("Number of rows is different")

        except:
            raise ValueError('Not a matrix')

    def __mul__(self, other):

        if type(other) == int:
            return Matrix([[other * i for i in n] for n in self.matrix])

        try:
            rows_m1 = len(self.matrix)
            rows_m2 = len(other.matrix)
            cols_m1 = len(self.matrix[0])
            cols_m2 = len(other.matrix[0])

            if cols_m1 == rows_m2:
                return Matrix([[sum(a * b for a, b in zip(row_m1, col_m2)) for col_m2 in zip(*other.matrix)]
                               for row_m1 in self.matrix])
            else:
                raise ValueError('Order not correct')
        except:
            raise ValueError

    def __rmul__(self, other):
        return self * other
