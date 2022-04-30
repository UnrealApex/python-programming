import random
def martix(x):
  for i in range(x):
    print("[", end="")
    for i in range(x):
      print(f" {random.randint(0, 1)} ", end="")
      
    print("]", end="")
    print("")  
