# Show the date saved in a tuple with a correct format

event_date = (2024, 12, 17)
print("The event will be in:", event_date)
print("The event will be in: %i/%i/%i" % event_date)

year, month, day = event_date
print("The event will be in: {}/{}/{}".format(day, month, year))
