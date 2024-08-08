# Obtain date and hours

import datetime

date = datetime.datetime.now()
print(date)

print(date.strftime("%d/%m/%Y %H:%M:%S"))