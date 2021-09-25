from matrix import Matrix
import contextlib


@contextlib.contextmanager
def read_file(filename, mode):
    my_file = open(filename, mode)  # Executed before the block

    yield my_file

    my_file.close()  # Executed after the block


# Reading matrix from file
def read_matrix(filename):
    matrix = []

    with read_file(filename, 'r') as fp:
        for line in fp:
            matrix.append([int(num) for num in line.split()])

    return matrix


matrix1 = Matrix(read_matrix('matrix1.txt'))
matrix2 = Matrix(read_matrix('matrix2.txt'))
