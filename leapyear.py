import sys
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

if __name__ == "__main__":
    year = int(sys.argv[1])

    if isLeapYear(year):
        print("Leap Year")
    else:
        print("Not a Leap Year")

    print(sys.argv[0])