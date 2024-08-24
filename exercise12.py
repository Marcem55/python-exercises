# Show the calendar of a year and month
import calendar

year = int(input("Enter a year in number: "))
month = int(input("Enter a month in number: "))
if month < 1 or month > 12:
    print("Enter a valid month")
else:
    print(calendar.month(year, month))