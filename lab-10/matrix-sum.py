import random
matrix = [[random.randint(0, 1) for i in range(4)] for j in range(4)]
print(matrix)
print(f"Largest row index: {matrix.index(max(matrix))}")
