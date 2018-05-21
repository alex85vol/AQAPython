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
def account_provider(request):
    print("Providing Banking Account {}".format(BankSupport))
    Config.account_provider = BankSupport
    def fin():
        del Config.account_provider

    request.addfinalizer(fin)

@pytest.fixture(scope="module", autouse=True)
def card_provider(request):
    print("Providing Card types enumeration")
    Config.card_provider = CardsKinds

    def fin():
        del Config.card_provider

    request.addfinalizer(fin)

def test_no_card():
    card_kind = Config.account_provider(0).card_kind
    assert card_kind == Config.card_provider.NO_CARD, "Incorrect type of card has been returned: {}. Should be {}".format(card_kind, Config.card_provider.NO_CARD)

def test_normal_card():
    card_kind = Config.account_provider(1).card_kind
    assert card_kind == Config.card_provider.NORMAL_CARD, "Incorrect type of card has been returned: {}. Should be {}".format(card_kind, Config.card_provider.NORMAL_CARD)

def test_gold_card():
    card_kind = Config.account_provider(10001).card_kind
    assert card_kind == Config.card_provider.GOLD_CARD, "Incorrect type of card has been returned: {}. Should be {}".format(card_kind, Config.card_provider.GOLD_CARD)

def test_platinum():
    card_kind = Config.account_provider(10001).card_kind
    assert card_kind == Config.card_provider.GOLD_CARD, "Incorrect type of card has been returned: {}. Should be {}".format(card_kind, Config.card_provider.GOLD_CARD)

def test_negative_debet(check_exception):
    negative_debet = -10.0
    assert check_exception(Config.account_provider, IncorrectDebetError, negative_debet), "Exception IncorrectDebetError hasn't been raised when created account with negative debet {}".format(str(negative_debet))

def test_take_more_then(check_exception):
    assert check_exception(Config.account_provider(100).take_founds, TakeMoneyUnavailabilityError, 101), "Exception TakeMoneyUnavailabilityError hasn't been raised when taken funds more then money is on the debet"
