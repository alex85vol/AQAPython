import pytest

from bank_support.BankSupport import BankSupport
from bank_support.CardsKinds import CardsKinds
from bank_support.Exceptions import IncorrectDebetError, TakeMoneyUnavailabilityError


@pytest.fixture
def check_exception():
    def checker(function, exception: Exception, *args):
        try:
            function(*args)
        except exception:
            return True
        except Exception:
            return False
        return False

    return checker


@pytest.fixture
def account_provider():
    return BankSupport


@pytest.fixture
def card_provider():
    return CardsKinds


def test_no_card(account_provider, card_provider):
    card_kind = account_provider(0).card_kind
    assert card_kind == card_provider.NO_CARD, "Incorrect type of card has been returned: {}. Should be {}".format(
        card_kind, card_provider.NO_CARD)


def test_normal_card(account_provider, card_provider):
    card_kind = account_provider(1).card_kind
    assert card_kind == card_provider.NORMAL_CARD, "Incorrect type of card has been returned: {}. Should be {}".format(
        card_kind, card_provider.NORMAL_CARD)


def test_gold_card(account_provider, card_provider):
    card_kind = account_provider(10001).card_kind
    assert card_kind == card_provider.GOLD_CARD, "Incorrect type of card has been returned: {}. Should be {}".format(
        card_kind, card_provider.GOLD_CARD)


def test_platinum(account_provider, card_provider):
    card_kind = account_provider(10001).card_kind
    assert card_kind == card_provider.GOLD_CARD, "Incorrect type of card has been returned: {}. Should be {}".format(
        card_kind, card_provider.GOLD_CARD)


def test_negative_debet(account_provider, check_exception):
    negative_debet = -10.0
    assert check_exception(account_provider, IncorrectDebetError,
                           negative_debet), "Exception IncorrectDebetError hasn't been raised when created account with negative debet {}".format(
        str(negative_debet))


def test_take_more_then(account_provider, check_exception):
    assert check_exception(account_provider(100).take_founds, TakeMoneyUnavailabilityError,
                           101), "Exception TakeMoneyUnavailabilityError hasn't been raised when taken funds more then money is on the debet"
