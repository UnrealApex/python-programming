pounds = float(input("Enter weight in pounds: "))
inches = float(input("Enter height in inches: "))
def lb_to_kg(value):
  global kilograms
  kilograms = value / 2.205
  return kilograms
def in_to_km(value):
  global kilometers
  kilometers = value / 39.37
  return kilometers
lb_to_kg(pounds)
in_to_km(inches)
bmi = kilograms / kilometers**2
print(f"You BMI is {bmi:.3f}")
