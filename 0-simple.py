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
