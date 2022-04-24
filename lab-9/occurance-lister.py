# list of numbers
numbers = input("Enter integers between 1 and 100 with a space between each: ").split(" ")
# distinct numbers in list that we will use to count occurances
y = set(numbers)
# make sure that all the numbers in the list are between 1 and 100
if (all(int(i) > 1 and int(i) < 100 for i in y)):
  # loop through the distinct numbers in the list and check how many times they occur in the list of numbers
  for i in y:
    # if the number is greater than 1, print times in plural form
    if int(i) > 1 or int(i) < 1:
      print(f"{i} occurs {numbers.count(i)} times")
    # if the number is 1, print times in singular form

    else:
      print(f"{i} occurs {numbers.count(i)} time")
else:
  print("Try Again!\n Make sure you enter numbers between 1 and 100")
