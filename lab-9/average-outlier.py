# list of numbers
numbers = input(
    "Enter a set a numbers to find the outliers in the group: ").strip().split(" ")
average = 0
# numbers at average
at_average = 0
# numbers above average
above_average = 0
# numbers below average
below_average = 0
# computer the average of the numbers in the list
for i in numbers:
    average += int(i)
average = average / len(numbers)

# compute how many numbers are at, above, and below the average
for i in numbers:
  if int(i) > average:
    above_average += 1
  elif int(i) < average:
    below_average += 1
  else:
    at_average += 1

# print the results
print(f"The average of the numbers in the set is {average}\n\
{at_average} numbers are equal to the average\n\
{above_average} numbers are above the average\n\
{below_average} numbers are below the average")
