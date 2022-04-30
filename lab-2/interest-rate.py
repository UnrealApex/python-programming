investment_amount = float(input("Enter investment ammount: "))
interest_rate = float(input("Enter annual interest rate: ")) / 100 
years = int(input("Enter number of years: "))
print(f"The acculmulated value is {investment_amount * (1 + interest_rate)**years}")
