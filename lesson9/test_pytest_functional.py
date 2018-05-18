import pytest


def test_1():
    assert 2 * 2 == 2 + 2


def test_2():
    assert 3 * 3 <= 3 + 3


def test_3():
    with pytest.raises(ZeroDivisionError):
        45 / 0
