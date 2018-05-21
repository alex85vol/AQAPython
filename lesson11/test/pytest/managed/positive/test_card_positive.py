from bank_support.CardsKinds import CardsKinds


class TestCardsPositive(object):
    def test_card(self, funds: float, expected_card_kind: CardsKinds):
        card_kind = self.bank_account(funds).card_kind
        assert card_kind.value == expected_card_kind.value, "Incorrect type of card has been returned: {}. Should be {}. Funds: {}".format(
            card_kind, expected_card_kind, str(funds))