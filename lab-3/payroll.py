# note that some of the decimal points are rounded up to the hundreths place so they follow the price format: xx.xx
# get our inputs
name = str(input("Enter employee's name: "))
hours_worked = float(input("Enter number of hours worked in a week: "))
pay_rate = float(input("Enter hourly pay rate: "))
# federal tax withholding
f_tax_withholding = float(input("Enter federal tax withholding rate: "))
# state tax withholding
s_tax_withholding = float(input("Enter state tax withholding rate: "))
gross_pay = pay_rate * hours_worked
# print the output formatted and put each line literally on a new line to improve the readability of this very long print statement/f string
print(f"----\n\n\
      Employee name: {name}\n\
      Hours worked: {hours_worked}\n\
      Pay rate: ${pay_rate:.2f}\n\
      Gross pay: ${gross_pay:.2f}\n\
      Deductions:\n\
      \tFederal Withholding ({f_tax_withholding * 100}%): ${gross_pay * f_tax_withholding:.2f}\n\
      \tState Withholding ({s_tax_withholding * 100}%): ${gross_pay * s_tax_withholding:.2f}\n\
      \tTotal deduction: ${gross_pay * (f_tax_withholding + s_tax_withholding):.2f}\n\
      Net pay: ${(1 - (f_tax_withholding + s_tax_withholding)) * gross_pay:.2f}")
