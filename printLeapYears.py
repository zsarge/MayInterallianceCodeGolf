def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 1:
            print(year)

for x in range(2021, 2040):
    isLeapYear(x)
