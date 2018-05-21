import pytest
import random
from bank_support.BankSupport import BankSupport
from bank_support.CardsKinds import CardsKinds
from bank_support.Exceptions import IncorrectDebetError, TakeMoneyUnavailabilityError

#pytest -v --setup-show --debug test/pytest/TestBankSupportWithFixtureScopeTuning.py

class Config(object):
    card_provider = None
    account_provider = None


class account_card_type_data_provider(object):
    def __init__(self):
        self.cards = (CardsKinds.NO_CARD, CardsKinds.NORMAL_CARD, CardsKinds.GOLD_CARD, CardsKinds.PLATINUM_CARD)
        print("Cards: {}".format(self.cards))

    def __call__(self, normal_threshold, gold_threshold, platinum_threshold):
        tmp = list()
        thresholds = ((0, 0),
                      (1, normal_threshold),
                      (normal_threshold + 1, gold_threshold),
                      (gold_threshold + 1, platinum_threshold),
                      (platinum_threshold + 1, 100000))

        for i in self.cards:
            ind = thresholds[self.cards.index(i)]
            for k in range(3):
                print("{}: {} -> {}".format(str(ind[0]), str(ind[1]), i))
                tmp.append((random.randint(ind[0], ind[1]), i))
        return tuple(tmp)


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

@pytest.fixture(scope="session", autouse=True)
def account_provider():
    Config.account_provider = BankSupport

@pytest.fixture(scope="module", autouse=True)
def card_provider():
    Config.card_provider = CardsKinds


@pytest.mark.parametrize("funds, expected_card_kind", account_card_type_data_provider()(10000, 100000, 10000000))
def test_card(funds: int, expected_card_kind: CardsKinds):
    card_kind = Config.account_provider(funds).card_kind
    assert card_kind == expected_card_kind, "Incorrect type of card has been returned: {}. Should be {}. Funds: {}".format(
        card_kind, expected_card_kind, str(funds))

@pytest.mark.parametrize("method, param, exception", ((BankSupport, -10, IncorrectDebetError),
                         (BankSupport(100).take_founds, 101, TakeMoneyUnavailabilityError)))
def test_negative_debet(check_exception, method, param, exception: Exception):
    assert check_exception(method, exception, param), "Exception IncorrectDebetError hasn't been raised"