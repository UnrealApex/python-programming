# program inputs
pounds = float(input("Enter weight in pounds: "))
inches = float(input("Enter height in inches: "))
#        kilograms           kilometers
bmi = ((pounds / 2.205)) / ((inches / 39.37)**2)
# print the output and format it using an f string
print(f"You BMI is {bmi:.3f}")
