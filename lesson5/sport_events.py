import datetime


class SportEvents(object):
    next_olympiade_date = datetime.date(2022, 2, 4)

    @classmethod
    def how_many_days_to_olympiade(cls):
        return (cls.next_olympiade_date - datetime.date.today()).days


if __name__ == '__main__':
    print(SportEvents.how_many_days_to_olympiade())
