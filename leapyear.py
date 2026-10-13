import syc

def leapyear(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

if __name__ == "__main__":
    y = int(syc.argv[1])

    if leapyear(y):
        print("Leap year")
    else:
        print("Not a leap year")

    print(syc.argv[0])