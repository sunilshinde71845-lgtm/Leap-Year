from leapyear import isLeapYear

def test_leap_year():
    assert isLeapYear(2024) == True

def test_not_leap_year():
    assert isLeapYear(2025) == False

def test_century_leap_year():
    assert isLeapYear(2000) == True