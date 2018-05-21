import pytest
from bank_support.BankSupport import BankSupport


@pytest.fixture(scope="class", autouse=True)
def account_provider(request):
    request.cls.bank_account_provider = BankSupport