import divisibleby

def test_divby5_1():
    x = 5
    result = divisibleby.divby5(x)
    assert result == "Divisible by 5"

def test_divby5_2():
    x = 7
    result = divisibleby.divby5(x)
    assert result == "not divisible"

def test_divby7_1():
    x = 14
    result = divisibleby.divby7(x)
    assert result == "Divisible by 7"

def test_divby7_2():
    x = 12
    result = divisibleby.divby7(x)
    assert result == "not divisible"

def test_divby9_1():
    x = 18
    result = divisibleby.divby9(x)
    assert result == "Divisible by 9"

def test_divby9_2():
    x = 20
    result = divisibleby.divby9(x)
    assert result == "not divisible"

def test_divby10_1():
    x = 20
    result = divisibleby.divby10(x)
    assert result == "Divisible by 10"

def test_divby10_2():
    x = 12
    result = divisibleby.divby10(x)
    assert result == "not divisible"