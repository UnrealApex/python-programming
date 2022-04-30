def reverse_int(x):
  i = (len(str(x)) - 1)
  while i >= 0:
    print(str(x)[i], end="")
    i -= 1