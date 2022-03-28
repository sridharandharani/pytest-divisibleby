import divisibleby
import pytest

@pytest.fixture
def input():
    x = 20
    return x

def test_divby5_1(input):
    result = divisibleby.divby5(input)
    assert result == "Divisible by 5"

def test_divby5_2(input):
    result = divisibleby.divby5(input)
    assert result == "not divisible"

def test_divby7_1(input):
    result = divisibleby.divby7(input)
    assert result == "Divisible by 7"

def test_divby7_2(input):
    result = divisibleby.divby7(input)
    assert result == "not divisible"

def test_divby9_1(input):
    result = divisibleby.divby9(input)
    assert result == "Divisible by 9"

def test_divby9_2(input):
    result = divisibleby.divby9(input)
    assert result == "not divisible"

def test_divby10_1(input):
    result = divisibleby.divby10(input)
    assert result == "Divisible by 10"

def test_divby10_2(input):
    result = divisibleby.divby10(input)
    assert result == "not divisible"