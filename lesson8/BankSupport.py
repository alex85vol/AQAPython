from random import randint

from CardsKinds import CardsKinds
from Exceptions import IncorrectDebetError, TakeMoneyUnavailabilityError


class BankSupport(object):
    def __init__(self, account_debet=0.0):
        self.account_id = randint(10000, 99999)
        self.account_debet = account_debet

    @property
    def card_kind(self):
        if self.account_debet < 0.0:
            raise IncorrectDebetError("Bank account #{}. Debet is under zero: {}".format(str(self.account_id), str(self.account_debet)))
        elif self.account_debet == 0.0:
            return CardsKinds.NO_CARD
        elif self.account_debet > 0.0 and self.account_debet <= 9000.0:
            return CardsKinds.NORMAL_CARD
        elif self.account_debet > 10000.0 and self.account_debet <= 99999.0:
            return CardsKinds.GOLD_CARD
        return CardsKinds.PLATINUM_CARD

    def charge_account(self, sum: float):
        if self.account_debet < 0.0:
            raise IncorrectDebetError("Bank account #{}. Debet is under zero: {}".format(str(self.account_id), str(self.account_debet)))
        self.account_debet += sum

    def take_founds(self, sum: float):
        if self.account_debet < 0.0:
            raise IncorrectDebetError("Bank account #{}. Debet is under zero: {}".format(str(self.account_id), str(self.account_debet)))
        elif self.account_debet < sum:
            raise TakeMoneyUnavailabilityError("Bank account #{}. Sum to take {} is more than your debet: {}".format(str(self.account_id), str(sum), str(self.account_debet)))
        self.account_debet -= sum