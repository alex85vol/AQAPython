import unittest
from functools import wraps

from lesson8.BankSupport import BankSupport
from lesson8.CardsKinds import CardsKinds
from lesson8.Exceptions import IncorrectDebetError, TakeMoneyUnavailabilityError


def test_with_card(card_type):
    def test_decorator(func):
        @wraps(func)
        def decorated(self, *args, **kwargs):
            res = func(self, *args, **kwargs).card_kind
            self.assertEqual(res, card_type,
                             "Incorrect type of card has been returned: {}. Should be {}".format(res, card_type))

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

    @test_with_card(CardsKinds.NO_CARD)
    def test_no_card(self):
        return self.bank_account(0)

    @test_with_card(CardsKinds.NORMAL_CARD)
    def test_normal_card(self):
        return self.bank_account(1)

    @test_with_card(CardsKinds.GOLD_CARD)
    def test_gold_card(self):
        return self.bank_account(10001)

    @test_with_card(CardsKinds.PLATINUM_CARD)
    def test_platinum(self):
        return self.bank_account(100001)

    @expect_exception(IncorrectDebetError)
    def test_negative_debet(self):
        self.bank_account(-10.0)

    @expect_exception(TakeMoneyUnavailabilityError)
    def test_take_more_then(self):
        self.bank_account(100).take_founds(1001)


if __name__ == '__main__':
    unittest.main()
