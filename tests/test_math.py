import pytest


@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2


@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == 3


@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as zerodiv:
        num = 1 / 0
    assert 'division by zero' in str(zerodiv.value)


products = [
    (3, 2, 6),  # two positive int
    (1, 10, 10),  # any number by 1
    (0, 5, 0),  # any number by 0
    (5, -5, -25),  # + * -
    (-5, -5, 25),  # - * -
    (3.2, 2.4, 7.68)  # Float numbers
]


@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_mult_properties(a, b, product):
    assert a * b == product