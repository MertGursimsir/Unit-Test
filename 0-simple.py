from doctest import Example
from lib2to3.pgen2.token import DOUBLESTAR

import pytest

# PROD CODE
def str_len(theStr):
    return len(theStr)

# UNIT TEST
def test_string_length():
    testStr = "1"               # SETUP
    result = str_len(testStr)   # ACTION
    assert result == 1          # ASSERT

# TESTS ARE WRITTEN BEFORE THE PRODUCTION CODE
# WRITE TEST - WRITE RELATIVE SMALL PART ...

# RED --> GREEN --> REFACTOR --> RED...
#   --> write failing unit test 
#   --> write just enough prod code to make that test pass
#   --> refactor test and code to make it clean

##### NAMING #####
# Test functions should start with "test"
# Test classes should start with "Test" and not have an __init__ method
# Filenames should start or end with "test"

# Tests can be run with "pytest" command
#   -v --> verbose mode
#   -q --> quiet mode (helpful for thousands of tests)
#   -s --> to see console output
#   --ignore --> ignores specified path when discovering tests
#   --maxfail --> stop after specified number of failures
#   -k --> matches tests found that match the evaluatable expression in the string
#          String values can include module, class, and function names
#          -k "test2 or test3"
#   -m --> runs the marked tests that match the evaluatable expression
#          You can mark the test with "@pytest.mark.test1" as test1



##### XUNIT #####
# setup_module() - teardown_module()
# setup_function() - teardown_function()
# setup_class() - teardown_class()
# setup_method() - teardown_method()

###### TEST FIXTURES #####
# 4 different scopes to specify how often fixture will be called:
#   function: run the fixture once for each test
#   class: once for each class of tests
#   module: when the module goes in scope
#   session: when pytest starts
# Fixtures can return data which can be used in test
#   optional params array argument in decorator can be used to specify data returned to the test
#   test will be called each element in params array



# Comparing 2 floating point numbers:
#   val = 0.1 + 0.2
#   assert val == approx(0.3)  ---> with a defaul tolerance of 1e-6


# Verify if a function throws an exception:
# def test_Exception():
#   with raises(ValueError):
#       raise ValueError
# If ValueError is not raised, test fails.
# Here it "raise ValueError" so no problem



# TEST DOUBLES
# Almost all code depends on other systems.
# Other systems are not easy to replicate or slows the test.
# TEST DOUBLES are OBJECTS that are used in unit tests as
#   replacements to the real production system collaborators.
# OBJECT TYPES
#   Dummy: Placeholders intended to be passed around but not
#           called or used in real. Do not have implementations.
#          Generate exception if called.
#   Fake: Simplified functional implementation.
#         Adequate for testing but not for production.
#   Stub: Provide implementations expected to be called, but
#           respond with basic canned responses.
#   Spies: Provide implementations that record the values
#           that were passed in to them.
#          Then tests use those recorded values to validate test.
#   Mocks: These objects are pre-programmed to expect about the
#           ordering of calls, number of times functions will be
#           called, values that will be passed in and can throw
#           exceptions when necessary.


# MOCK FRAMEWORKS: Libs that provide easy to use APIs
#   Provides easy ways for automatically creating any of these
#     types of test doubles at runtime.
#   Better than creating mock objects by hand because this can
#     be tedious and error-prone.


# unittest.mock
#   PYTHON MOCKING FRAMEWORK
#   Provides Mock() class which can be used as a
#       fake, stub, spy, or true mock for all your tests.
#   Mock has many initialization parameters to specify
#       how the Mock object should behave.
#   Once called, a Mock object has many functions to verify
#       how it was used.

# Example
def test_Foo():
    bar = Mock()
    functionThatUsesBar(bar)
    bar.assert_called_once()

    bar = Mock(spec=SpecClass)
    # Specifies the interface that Mock object is implementing.
    # If any attributes of the mock Object are called which are
    #   not in that interface, mock will generate an attribute exception.

    bar2= Mock(side_effect=barFunc)
    # Function that should be called when the mock is called.

    bar3= Mock(return_value=1)
    # Specifies return value when mock is called.
    # If side_effect is set, its return value is used.

# VERIFICATION
# assert_called --> Assert the mock was called.
# assert_called_once --> mock was called exactly one time
# assert_called_with --> last call to mock was with specified params
# assert_called_once_with --> mock called once with specified params
# assert_any_call --> mock was ever called with the specified params
# assert_not_called --> mock was not called
# assert_has_calls --> mock was called with the list of calls.
################################################################
# called --> boolean, true if mock is ever called
# call_count --> number of times mock was called
# call_args --> arguments the mock was last called with
# call_args_list --> list with each entry containing the params
#   that were used in a call to mock object.

# MagicMock CLASS
# derived from Mock and provides a default implementation of many
#   of the default magic methods defined for objects in Python
#   such as __str__
# These are not implemented: __getattr__, __setattr__, __init__,
#   __new__, __prepare__, __instancecheck__, __subclasscheck__,
#   __del__
#


# PyTest monkeypatch Text Fixture
def callIt():
    print("hello world")

def test_path(monkeypatch):
    monkeypatch(callIt, Mock())
    callIt()
    callIt.assert_called_once()
# Allow a test to dynamically replace:
#   module and class attributes
#   dictionary entries
#   environment variables



####################
# - Keep console output minimum
# - Write tests incrementally more complex, start from simple
# - Make tests understandable
# - Run tests multiple times in random order (they should not have any dependency)
#       pytest-repeat & pytest-random-order plugins
# - Use static code analysis tools also like pylint
# - Use code coverage tools to see if tests are adequent
# - Test behaviour rather than implementation

## Example
def addDays(theDate, days):
    return theDate.timedelta(days=days)

# This method is testing via the implementation
def test_addDasyImplementation(monkeypatch):
    mock_delta = MagicMock(return_value=datetime.timedelta(days=1))
    monkeypatch(datetime.timedelta, mock_delta)
    addDays(datetime.datetime(2020, 1, 1), 1)
    mock_delta.assert_called_once_with(days=1)

# This method tests behaviour rather than implementation
def test_addDasyImplementation2(monkeypatch):
    result = addDays(datetime.datetime(2020, 1, 1), 1)
    assert result == datetime.datetime(2020, 1, 2)
