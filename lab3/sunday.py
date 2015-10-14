def checkSun(day):
  if day%7 == 0:
    return True

day = 1
date = 1
year = 1900
month = 1
sundays = 0

while year <= 2000:
  if month == 12 and date == 31:
    year = year+1

  if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if date == 31:
      month = month+1
      date = 1
  elif month == 4 or month == 6 or month == 9 or month == 11:
    if date == 30:
        month = month+1
        date = 1
  elif month == 2 and year%4 != 0:
    if date == 28:
        month = month +1
        date = 1
  elif month == 2 and year%4 == 0 and year%400 != 0:
    if date == 29:
        month = month+1
        date = 1
  elif month == 2 and year%400 == 0:
    if date == 28:
        month = month+1
        date = 1

  if date == 1 and checkSun(day):
    sundays = sundays +1
  day = day+1

print(sundays)