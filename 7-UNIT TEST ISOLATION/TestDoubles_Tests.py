import pytest
from pytest import raises
from unittest.mock import MagicMock
from LineReader import readFromFile

# def test_canCallReadFromFile():
#     readFromFile("mert")

# We will mock out the open function that opens file to return a MagicMock object
# and add readline attribute to mock to return test string

@pytest.fixture
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open

# mock_open is fixture parameter name
# that fixture will be called and return value will be assigned to mock_open
def test_returnsCorrectString(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    # real os.path.exists check file if mock_exists doesn't defined

    result = readFromFile("mert")
    mock_open.assert_called_once_with("mert", "r")
    # Checks that open() was called once, with exactly those arguments.
    assert result == "test line"

def test_throwExceptionWithBadFile(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)

    with raises(Exception):
        result = readFromFile("mert")