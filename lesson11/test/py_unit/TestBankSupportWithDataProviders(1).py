import unittest

from functools import wraps

from bank_support.BankSupport import BankSupport
from bank_support.CardsKinds import CardsKinds
from bank_support.Exceptions import IncorrectDebetError, TakeMoneyUnavailabilityError


def test_with_card(data_tuple: tuple):
    def test_decorator(func):
        @wraps(func)
        def decorated(self, *args, **kwargs):
            for data in data_tuple:
                fund = data[0]
                card_type = data[1]
                res = func(self, fund).card_kind
                self.assertEqual(res, card_type, "Incorrect type of card has been returned: {}. Should be {}".format(res, card_type))
        return decorated
    return test_decorator

def expect_exception(exception):
    """Marks test to expect the specified exception. Call assertRaises internally"""
    def test_decorator(fn):
        def test_decorated(self, *args, **kwargs):
            self.assertRaises(exception, fn, self, *args, **kwargs)
        return test_decorated
    return test_decorator

class MyTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = CardsKinds

    @classmethod
    def tearDownClass(cls):
        del cls.cards

    def setUp(self):
        self.bank_account = BankSupport

    def tearDown(self):
        del self.bank_account

    @test_with_card(((0, CardsKinds.NO_CARD),
                     (1, CardsKinds.NORMAL_CARD),
                     (10001, CardsKinds.GOLD_CARD),
                     (100001, CardsKinds.PLATINUM_CARD)))
    def test_platinum(self, val):
        return self.bank_account(val)

    @expect_exception(IncorrectDebetError)
    def test_negative_debet(self):
        self.bank_account(-10.0)

    @expect_exception(TakeMoneyUnavailabilityError)
    def test_take_more_then(self):
        self.bank_account(100).take_founds(1001)


if __name__ == '__main__':
    unittest.main()
