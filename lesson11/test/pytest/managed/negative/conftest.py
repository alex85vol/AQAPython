from bank_support.BankSupport import BankSupport
from bank_support.Exceptions import IncorrectDebetError, TakeMoneyUnavailabilityError
import random


def pytest_generate_tests(metafunc):
    s = random.randint(0, 10000)
    metafunc.parametrize("method, param, exception", ((BankSupport, random.randint(-100, -1), IncorrectDebetError),
                         (BankSupport(s).take_founds, s + 1, TakeMoneyUnavailabilityError)))