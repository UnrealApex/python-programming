# import calendar
from calendar import *
print("days in a month calculator")
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
print(
    f"The month {month_name[month]} in the year {year} had {monthrange(year, month) [1]} days"
)
