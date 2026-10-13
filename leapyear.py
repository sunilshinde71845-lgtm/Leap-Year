def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

year = int(input("Enter year: "))

if isLeapYear(year):
    print("Leap Year")
else:
    print("Not a Leap Year")