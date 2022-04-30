def gfc(x , y):
  # keep getting the modulus of x and y until x is the gfc
  print(f"The greatest common factor of {x} and {y} is ", end="")
  while y != 0:
    x, y = y, x % y
  print(str(x))
