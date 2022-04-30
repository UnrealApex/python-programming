# arrays that store the values we'll manipulate
numbers = []
positive_numbers = []
negative_numbers = []
# our main loop that the program runs in
while True:
  # get an input number in the loop iteration
  x = input("Enter a whole number that is not 0 and press enter when finished: ")
  # if the user didn't enter a value or x isn't a number, break out of the loop 
  if (x == "" or int(x) == 0):
    # print("Rerun the program and enter a number!")
    # x = 0
    break
  else:
    # if x is zero, go to the next iteration of the loop because we don't need to do any calculations with it
    # if x is a positive number, add it to the positive numbers array
    if (int(x) > 0):
      numbers.append(int(x))
      positive_numbers.append(int(x))
    # if x is a negative number, add it to the negative numbers array
    elif (int(x) < 0):
      numbers.append(int(x))
      negative_numbers.append(int(x))
    # if something else happens, just pass  
    else:
      pass  
# if there are numbers in the numbers array and 0 is not one of the numbers, do the
calculations      
if ((numbers != []) and (0 not in numbers)):      
  print(f"\n\
The number of positive numbers given is {len(positive_numbers)}\n\
The number of negative numbers given is {len(negative_numbers)}\n\
{len(numbers)} numbers were given \n\
The average of the numbers given is {str((sum(numbers) / len(numbers)))} \
      ")
