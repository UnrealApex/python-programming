# list of numbers
numbers = input(
    "Enter a set of integers to find the distinct ones in the set ").strip().split(" ")
# convert each array item to the type integer
numbers = map(int, numbers)
# print the results
print(f"Distinct numbers are {set(numbers)}")
