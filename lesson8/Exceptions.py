class IncorrectDebetError(Exception):
    print('In custom debet exception')

    def __int__(self):
        return Exception


class TakeMoneyUnavailabilityError(Exception):
    pass
