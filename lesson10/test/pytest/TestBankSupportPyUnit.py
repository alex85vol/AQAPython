import pytest
import random
import unittest

from bank_support.BankSupport import BankSupport
from bank_support.CardsKinds import CardsKinds
from bank_support.Exceptions import IncorrectDebetError, TakeMoneyUnavailabilityError

@pytest.fixture(scope="function")
def check_exception():
    def checker(function, exception: Exception, *args):
        try:
            print("Checking for exception {} for function {}".format(exception, function.__name__))
            function(*args)
        except exception:
            return True
        except Exception:
            return False
        return False
    return checker

@pytest.fixture(scope="class")
def account_provider(request):
    class Config(object):
        def __init__(self):
            self.bank_account = BankSupport
            self.cards = CardsKinds

    request.cls.config = Config()

@pytest.mark.usefixtures("account_provider")
class MyTestSuite(unittest.TestCase):

    def test_no_card(self):
        card_kind = self.config.bank_account(0).card_kind
        self.assertEqual(card_kind, self.config.cards.NO_CARD, "Incorrect type of card has been returned: {}. Should be {}".format(card_kind, self.config.cards.NO_CARD))

    def test_normal_card(self):
        card_kind = self.config.bank_account(1).card_kind
        self.assertEqual(card_kind, self.config.cards.NORMAL_CARD,
                         "Incorrect type of card has been returned: {}. Should be {}".format(card_kind,
                                                                                             self.config.cards.NORMAL_CARD))
    def test_gold_card(self):
        card_kind = self.config.bank_account(10001).card_kind
        self.assertEqual(card_kind, self.config.cards.GOLD_CARD,
                         "Incorrect type of card has been returned: {}. Should be {}".format(card_kind,
                                                                                             self.config.cards.GOLD_CARD))
    def test_platinum(self):
        card_kind = self.config.bank_account(100001).card_kind
        self.assertEqual(card_kind, self.config.cards.PLATINUM_CARD,
                         "Incorrect type of card has been returned: {}. Should be {}".format(card_kind,
                                                                                             self.config.cards.PLATINUM_CARD))
    def test_negative_debet(self):
        negative_debet = -10.0
        with self.assertRaises(IncorrectDebetError):
            self.config.bank_account(negative_debet)

    def test_take_more_then(self):
        normal_account = self.config.bank_account(100)
        with self.assertRaises(TakeMoneyUnavailabilityError):
            normal_account.take_founds(1001)