# program that generates a 4x4 matrix filled with ones and zeros and prints out
# which rows and columns have the greatest amount of ones and zeros
import random
matrix = [[random.randint(0, 1) for i in range(4)] for j in range(4)]
print(matrix)
rows = [[row[0] for row in matrix]]
rows.sort()
print(f"Largest row index: {matrix.index(max(matrix))}")
print(f"Largest column index: {rows[-1]})")
