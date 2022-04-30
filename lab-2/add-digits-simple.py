# get user input
x = int(input("Enter a number between 0 and 1000: "))
# sum to print out
sum = 0
# checks if the input number meets assignment requirements of being between 0 and 
100
if (x >= 0 and x <= 1000):
  # iterate done stripping out numbers
  while x != 0:
    # get the value of the last place of the last digit
    sum += x % 10
    # extract number 
    x //= 10
  # prints out the sum when the while loop has finished executing  
  print(sum)
# print this message if the user didn't enter a number that was between 0 and 1000
else:
  print("Rerun and enter a number between 0 and 1000")
