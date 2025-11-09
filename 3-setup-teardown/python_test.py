# pytest calls setup and teardown functions for each test
def setup_function(function):
    if function == test1:
        print("\nSetting up test1!")
    elif function == test2:
        print("\nSetting up test2!")
    else:
        print("\nSetting up unknown test!")

def teardown_function(function):
    if function == test1:
        print("\nTearing down test1!")
    elif function == test2:
        print("\nTearing down test2!")
    else:
        print("\nTearing down unknown test!")
##################################################

# before and after all the unit tests have completed
def setup_module(module):
    print("\nSetting up module!", module)
def teardown_module(module):
    print("\nTearing down module!")
##################################################

def test1():
    print("Executing test1!")
    assert True

def test2():
    print("Executing test2!")
    assert True