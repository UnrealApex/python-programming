# sum of digits adder
def addDigits():
  x = int(input("Enter a number between 0 and 1000: "))
  if x >= 0 and x <= 1000:
    # separate the input into an array of string numbers and convert array items to integers so we can add them
    digits = list(map(int, list(str(x))))
    sum = 0
    for i in range(len(digits)):
      sum += digits[i]
    
    print("The sum of the digits of the number is " + str(sum))
  else:
    print("Enter a number between 0 and 1000!")
# main loop
while True:
  try:
    addDigits()
    run_again = str(input("Want to try again?\n [y]es or [n]o: "))
    if (not(run_again.lower() == "y" or run_again.lower() == "yes")):
      print("Program stopped")
      break
# keep running if the user triggers an exception
  except:
    print("Enter a number")
    pass
