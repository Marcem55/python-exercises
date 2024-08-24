# Calculate the days difference between 2 dates

from datetime import date
today = date(2024, 8, 24)
my_birthday = date(2024, 12, 17)

difference = my_birthday - today
print(difference.days)