import datetime

sundays = 0

for year in range(1901, 2001):
    for month in range(12):
        if datetime.date(year, month + 1, 1).weekday() == 6:
            sundays += 1

print sundays

