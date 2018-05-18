import pytest

class TestFirst(object):
    def test_1(self):
        assert 2 * 2 == 2 + 2
    
    def test_2(self):
        assert 3*3 <= 3 + 3
    
    def test_3(self):
        with pytest.raises(ZeroDivisionError):
            45 / 0
