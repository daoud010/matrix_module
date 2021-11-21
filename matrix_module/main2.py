from matrix import Matrix
import contextlib
from functools import wraps


# Generator function decorated
@contextlib.contextmanager
def read_file(filename, mode):  # Executed before the block
    my_file = open(filename, mode)

    yield my_file

    my_file.close()


# Reading matrix from file
def read_matrix(filename):
    matrix = []

    with read_file(filename, 'r') as fp:
        for line in fp:
            matrix.append([int(num) for num in line.split()])

    return matrix


# Reading Matrices
matrix1 = Matrix(read_matrix('matrix1.txt'))
matrix2 = Matrix(read_matrix('matrix2.txt'))


# Priming a coroutine
def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        generator = func(*args, **kwargs)
        next(generator)
        return generator

    return primer


# Adding matrices in series
@coroutine
def add_series():
    result = Matrix(None)

    while True:
        curr_matrix = yield result

        if result.matrix is None:
            result.matrix = curr_matrix.matrix
            result.print()
        else:
            try:
                result = curr_matrix + result
            except:
                print('Cannot add.')
            else:
                result.print()


@coroutine
def multiply_series():
    result = Matrix(None)

    while True:
        curr_matrix = yield result

        if result.matrix is None:
            result.matrix = curr_matrix.matrix
            result.print()
        else:
            try:
                result = curr_matrix * result
            except:
                print('Cannot multiply')
            else:
                result.print()


def switch():
    matrix = yield
    return matrix * matrix


# Multiplying matrices and adding in series
@coroutine
def switch_add_multiply():
    result = Matrix(None)

    while True:
        curr_matrix = yield from switch()

        if result.matrix is None:
            result.matrix = curr_matrix.matrix
            result.print()

        else:
            try:
                result = curr_matrix + result
            except:
                print('Order not correct')
            else:
                result.print()


# Multipyling matrices with scalar in series
@coroutine
def intensify_magnitude(matrix):
    result = matrix
    while True:
        value = yield result

        try:
            result = result * value
        except:
            print('Not possible')
        else:
            result.print()


"""
cr = add_series()
cr.send(matrix1)
cr.send(matrix2)
m = Matrix([0, 0])
cr.send(m)
cr.send(matrix1)
cr.close()
"""

"""
cr = multiply_series()
cr.send(matrix1)
cr.send(matrix2)
m = Matrix([[0, 0]])
cr.send(m)
cr.send(matrix1)
cr.close()
cr = switch_add_multiply()
cr.send(matrix1)
cr.send(matrix2)
cr.close()
"""

cr = intensify_magnitude(matrix1)
cr.send(2)
cr.send(3)
cr.close()
