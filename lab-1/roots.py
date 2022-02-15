# solution to the first question
print("a | a^2 | a^3")
for i in range(5):
    # go to the next iteration of the loop if i is 0 because squaring zero is zero
    if (i == 0):
        continue
    print(str(i**1) , str(i**2), str(i**3), sep=" | ")
