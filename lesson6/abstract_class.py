from abc import ABCMeta, abstractmethod


class Humano(metaclass=ABCMeta):
    def __index__(self, name, surname):
        self.name = name
        self.surname = surname

    @abstractmethod
    def eat(self, dish):
        pass

    def sleep(self):
        print("I'm sleeping")


class Womano(Humano):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def birth(self):
        pass

    def eat(self):
        print("I'm eating till 6 PM")


class Mano(Humano):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def fight(self):
        pass


    def eat(self):
        print("I'm eating only healthy food")
