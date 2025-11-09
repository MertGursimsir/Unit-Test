from pytest import raises, approx

def functionThatRaisesError():
    raise ValueError("test")

def test_exception():
    with raises(ValueError):
        functionThatRaisesError()