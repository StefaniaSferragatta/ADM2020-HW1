import math

def is_leap(year):
    leap = False
    max = pow(10,5)
    if year in range (1900,max):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            leap = True
        else:
            leap = False
    return leap

year = int(input())
