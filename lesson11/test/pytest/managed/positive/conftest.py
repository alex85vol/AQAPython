import pytest

from bank_support.BankSupport import BankSupport
from build.lib.bank_support.CardsKinds import CardsKinds


def pytest_addoption(parser):
    parser.addoption("--input_data",
                     action='store',
                     help="Set the path to the input file with the test data")


def pytest_generate_tests(metafunc):
    params_list = list()
    with open(pytest.config.getoption('--input_data'), "r") as input_file:
        for line in input_file:
            vals = line.split(", ")
            params_list.append((float(vals[0]), CardsKinds(vals[1].strip())))
    metafunc.parametrize("funds, expected_card_kind", tuple(params_list))


@pytest.fixture(scope="class", autouse=True)
def account_provider(request):
    request.cls.bank_account = BankSupport