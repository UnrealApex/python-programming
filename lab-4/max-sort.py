print(
    "Enter three numbers to be sorted by least to greatest numerical value\n")
# inputs
x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
z = int(input("Enter your third number: "))
# store the inputs in an array
# sort the numbers by value ascending using the sorted function
print("Values given sorted:")
if x > (y and z):
    # print out the items of the array sorted_numbers in each loop iteration
    if (y > z):
        print(z)
        print(y)
    else:
        print(y)
        print(z)
    print(x)
elif y > (x and z):
    if (x > z):
        print(z)
        print(x)
    else:
        print(x)
        print(z)
    print(y)
else:
    if (x > y):
        print(y)
        print(x)
    else:
        print(x)
        print(y)
    print(z)
