class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def print(self):
        print(self.matrix)

    # Add matrices

    def __add__(self, other):

        try:
            rows_m1 = [len(self.matrix)]
            rows_m2 = [len(other.matrix)]
            cols_m1 = [len(self.matrix[0])]
            cols_m2 = [len(other.matrix[0])]

            if rows_m1 == rows_m2:
                if cols_m1 == cols_m2:
                    return Matrix([[col_m1+col_m2 for (col_m1, col_m2) in zip(row_m1, rows_m2)] for (row_m1, row_m2) in
                                  zip(self.matrix, other.matrix)])
                else:
                    raise ValueError("Number of rows is different")
            else:
                ValueError("Number of rows is different")

        except:
            raise ValueError('Not a matrix')

