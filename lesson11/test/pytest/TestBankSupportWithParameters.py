import pytest

from bank_support.BankSupport import BankSupport
from bank_support.CardsKinds import CardsKinds
from bank_support.Exceptions import IncorrectDebetError, TakeMoneyUnavailabilityError

#pytest -v --setup-show --debug test/pytest/TestBankSupportWithFixtureScopeTuning.py

class Config(object):
    card_provider = None
    account_provider = None

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
    print("Providing Banking Account {}".format(BankSupport))
    Config.account_provider = BankSupport

@pytest.fixture(scope="module", autouse=True)
def card_provider():
    print("Providing Card types enumeration")
    Config.card_provider = CardsKinds


@pytest.mark.parametrize("funds, expected_card_kind", ((0, CardsKinds.NO_CARD),
                         (1, CardsKinds.NORMAL_CARD),
                         (10001, CardsKinds.GOLD_CARD),
                         (100010, CardsKinds.PLATINUM_CARD)))
def test_card(funds: int, expected_card_kind: CardsKinds):
    card_kind = Config.account_provider(funds).card_kind
    assert card_kind == expected_card_kind, "Incorrect type of card has been returned: {}. Should be {}".format(
        card_kind, expected_card_kind)

@pytest.mark.parametrize("method, param, exception", ((BankSupport, -10, IncorrectDebetError),
                         (BankSupport(100).take_founds, 101, TakeMoneyUnavailabilityError)))
def test_negative_debet(check_exception, method, param, exception: Exception):
    assert check_exception(method, exception, param), "Exception IncorrectDebetError hasn't been raised"