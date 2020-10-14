import calendar

month, day, year = map(int, input().split())
if year in range (2000,3001):
    _weekday = calendar.weekday(year, month, day)
    if _weekday == 0:
        print ("MONDAY")
    elif _weekday == 1:
        print ("TUESDAY")
    elif _weekday == 2:
        print ("WEDNESDAY")
    elif _weekday == 3:
        print ("THURSDAY")
    elif _weekday == 4:
        print ("FRIDAY")
    elif _weekday == 5:
        print ("SATURDAY")
    else:
        print ("SUNDAY")

