import pytest


class TestIncorrectInput(object):
    def test_incorrect_input(self, method, param, exception: Exception):
        with pytest.raises(exception):
            method(param)