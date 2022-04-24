# list of numbers
numbers = input(
    "Enter integers between 1 and 100 with a space between each: ").strip().split(" ")
# convert each array item to the type integer
numbers = map(int, numbers)
# print the results
print(f"Distinct numbers are {set(numbers)}")
