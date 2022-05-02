# inputs
row_1 = input("Enter 3-by-4 matrix row for row 1: ").strip().split(" ")
row_2 = input("Enter 3-by-4 matrix row for row 2: ").strip().split(" ")
row_3 = input("Enter 3-by-4 matrix row for row 3: ").strip().split(" ")

# convert each value in the matrix rows to a float
row_1 = map(float, row_1) 
row_2 = map(float, row_2) 
row_3 = map(float, row_3) 

# print the result
print()
print(f"The sum of the elements for column 1 is {sum(row_1)}")
print(f"The sum of the elements for column 2 is {sum(row_2)}")
print(f"The sum of the elements for column 3 is {sum(row_3)}")
