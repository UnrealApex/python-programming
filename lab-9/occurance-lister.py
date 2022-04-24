numbers = input("Enter integers between 1 and 100 with a space between each: ").split(" ")
y = set(numbers)
if (all(int(i) > 1 and int(i) < 100 for i in y)):
  for i in y:
    if int(i) > 1:
      print(f"{i} occurs {numbers.count(i)} times")
    else:
      print(f"{i} occurs {numbers.count(i)} time")
else:
  print("Try Again!\n Make sure you enter numbers between 1 and 100")
