print(
    "Enter three numbers to be sorted by least to greatest numerical value\n")
# inputs
x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
z = int(input("Enter your third number: "))
# store the inputs in an array
numbers = [x, y, z]
# sort the numbers by value ascending using the sorted function
sorted_numbers = sorted(numbers)
print("Values given sorted:")
# loop through the array
for i in sorted_numbers:
    # print out the items of the array sorted_numbers in each loop iteration
    print(f"{i}")
