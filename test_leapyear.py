from leapyear import leapyear

def test_year1():
    assert leapyear(2024) == "Leap Year"

def test_year2():
    assert leapyear(2025) == "Not a Leap Year"

def test_year3():
    assert leapyear(2000) == "Leap Year"