# program that gets the index of the smallest number in a list

# list of numbers
numbers = input(
    "Enter a set of integers to find the distinct ones in the set: ").strip().split(" ")
# print the index of the smallest number in the list
print(numbers.index(min(numbers)))
