import os
from bank_support.BankSupport import BankSupport
from bank_support.CardsKinds import CardsKinds

def pytest_generate_tests(metafunc):
    params_list = list()
    with open(os.path.join(os.path.curdir, "test", "test_data", "input_data.txt"), "r") as input_file:
        for line in input_file:
            vals = line.split(", ")
            params_list.append((float(vals[0]), CardsKinds(vals[1].strip())))
    metafunc.parametrize("funds, expected_card_kind", tuple(params_list))

class TestBankAccount(object):
    def test_card(self, funds: int, expected_card_kind: CardsKinds):
        card_kind = BankSupport(funds).card_kind
        assert card_kind == expected_card_kind, "Incorrect type of card has been returned: {}. Should be {}. Funds: {}".format(
            card_kind, expected_card_kind, str(funds))