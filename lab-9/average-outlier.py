# list of numbers
numbers = input(
    "Enter a set a numbers to find the outliers in the group: ").strip().split(" ")
# computer the average of the numbers in the list
average = 0
at_average = 0
above_average = 0
below_average = 0
for i in numbers:
    average += int(i)
average = average / len(numbers)

for i in numbers:
  if int(i) > average:
    above_average += 1
  elif int(i) < average:
    below_average += 1
  else:
    at_average += 1

print(f"The average of the numbers in the set is {average}\n\
{at_average} numbers are equal to the average\n\
{above_average} numbers are above the average\n\
{below_average} numbers are below the average")
