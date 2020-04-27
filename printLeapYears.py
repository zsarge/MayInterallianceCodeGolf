# https://www.mathsisfun.com/leap-years.html

# Basic logic: no attempt at code golfing
def isLeapYear(year):
    if year % 4 == 0: # if it can be divided by four
        if year % 100 != 0 or year % 400 == 1: # and either can't be divided by 100 or can be divided by 400
            return True

for x in range(2040):
    print(f"{x} - {isLeapYear(x)}")
