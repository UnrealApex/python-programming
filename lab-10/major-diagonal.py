# program that prints the sum of the major diagonal of a matrix
def matrix_diagonal(matrix):
    if type(matrix) is not list or len(matrix) == 0:
        return None
    for i in matrix:
        if type(i) is not list or len(i) == 0:
            return None
        if len(i) != len(matrix[0]):
            return None
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum
