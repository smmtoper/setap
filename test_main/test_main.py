from main.main import is_even

def test_is_even_with_even_number():
    assert is_even(4) == True

def test_is_even_with_odd_number():
    assert is_even(5) == False

def test_is_even_with_zero():
    assert is_even(0) == True

def test_is_even_with_negative_even_number():
    assert is_even(-2) == True

def test_is_even_with_negative_odd_number():
    assert is_even(-3) == False
