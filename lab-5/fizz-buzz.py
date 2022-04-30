# set a count for how many numbers should be on a line
count = 0
# count from 100 to 201 because numbers in coding start from 0 not 1
for i in range(100, 201):
  # check if number is divisible by 5 or 6 but not divisible for both
  if (i % 5 == 0 or i % 6 == 0 and not(i % 5 == 0 and i % 6 == 0)):
    # tried to use the sep parameter here but it didn't work
    print(f" {i} ", end="")
    # increased number on line count
    count += 1
    # if there are 10 numbers on a line, go to the next one
    if count % 10 == 0:
      print("\n")
      # reset the count for the next line
      count = 0
    
