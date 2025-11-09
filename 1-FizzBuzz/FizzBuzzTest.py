import pytest

def fizzBuzz(value):
    if isMultiple(value, 15) == 0:
        return "FizzBuzz"
    elif isMultiple(value, 3) == 0:
        return "Fizz"
    elif isMultiple(value, 5) == 0:
        return "Buzz"
    return str(value)

def isMultiple(value, mod):
    return (value % mod) == 0

# SINCE OTHER TEST CASES ALREADY TESTS THIS,
# WE REMOVE THIS TEST AT REFACTOR PHASE
# def test_canCallFizzBuzz():
#     fizzBuzz(1)

def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal

def test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")

def test_returns2With2PassedIn():
    checkFizzBuzz(2, "2")

def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")

def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")

def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6, "Fizz")

def test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10, "Buzz")

def test_returnsFizzBuzzWith15PassedIn():
    checkFizzBuzz(15, "FizzBuzz")