import pytest

# @pytest.fixture(autouse=True)
#   This will apply fixture to all tests in the scope.
@pytest.fixture()
def setup1():
    print("\nSetup 1!")
    ## code after yield is executed after the fixture goes out of scope
    yield
    print("\nTeardown 1!")

@pytest.fixture()
def setup2(request):
    print("\nSetup 2!", request)

    def teardown_a():
        print("\nTeardown A!")

    def teardown_b():
        print("\nTeardown B!")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

def test1(setup1):
    print("Executing test1!")
    assert True

@pytest.mark.usefixtures("setup2")
def test2():
    print("Executing test2!")
    assert True