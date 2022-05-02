# program that prints the sum of the major diagonal of a matrix
def matrix_diagonal(matrix):
    # do nothing if the matrix passed is not a matrix
    if type(matrix) is not list or len(matrix) == 0:
        return None
    # loop through the matrix and make sure that each dimension is a matrix
    for i in matrix:
        if type(i) is not list or len(i) == 0:
            return None
        if len(i) != len(matrix[0]):
            return None
    # if the matrix passed is value, calculate the sum of all  the numbers in the major diagonal
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum
