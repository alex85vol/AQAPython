import unittest

from lesson8.BankSupport import BankSupport
from lesson8.CardsKinds import CardsKinds
from lesson8.Exceptions import IncorrectDebetError, TakeMoneyUnavailabilityError


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

    def test_no_card(self):
        card_kind = self.bank_account(0).card_kind
        self.assertEqual(card_kind, self.cards.NO_CARD,
                         "Incorrect type of card has been returned: {}. Should be {}".format(card_kind,
                                                                                             self.cards.NO_CARD))

    def test_normal_card(self):
        card_kind = self.bank_account(1).card_kind
        self.assertEqual(card_kind, self.cards.NORMAL_CARD,
                         "Incorrect type of card has been returned: {}. Should be {}".format(card_kind,
                                                                                             self.cards.NORMAL_CARD))

    def test_gold_card(self):
        card_kind = self.bank_account(10001).card_kind
        self.assertEqual(card_kind, self.cards.GOLD_CARD,
                         "Incorrect type of card has been returned: {}. Should be {}".format(card_kind,
                                                                                             self.cards.GOLD_CARD))

    def test_platinum(self):
        card_kind = self.bank_account(100001).card_kind
        self.assertEqual(card_kind, self.cards.PLATINUM_CARD,
                         "Incorrect type of card has been returned: {}. Should be {}".format(card_kind,
                                                                                             self.cards.PLATINUM_CARD))

    def test_negative_debet(self):
        negative_debet = -10.0
        with self.assertRaises(IncorrectDebetError):
            self.bank_account(negative_debet)

    def test_take_more_then(self):
        normal_account = self.bank_account(100)
        with self.assertRaises(TakeMoneyUnavailabilityError):
            normal_account.take_founds(1001)


if __name__ == '__main__':
    unittest.main()
