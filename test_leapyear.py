from leapyear import leapyear

def test_leapyear():
    assert leapyear(2024) == "Leap Year"

def test_leapyear():
    assert leapyear(2025) == "Not a Leap Year"

def test_leapyear():
    assert leapyear(2000) == "Leap Year"