def occuranceLister():
  x = input("Enter integers between 1 and 100 with a space between each: ")
  x = x.split(" ")
  for i in x:
    print(f"{i} occurs {x.count(i)} times")

occuranceLister()