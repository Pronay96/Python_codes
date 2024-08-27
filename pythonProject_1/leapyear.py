from dates import *

yr = int(input("Enter year as 4 digits (e.g: 2002): "))
mn = int(input("Enter month number: "))

year_type = is_leap(yr)
month_type = month_name(mn)
days_in_month = day_in_month(month_type, yr)

print(f"Year: {year_type}")
print(f"Month Name: {month_type}")
print(f"Days in month: {days_in_month}")