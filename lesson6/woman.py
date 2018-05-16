from lesson6.inheritance import Human06


class Woman(Human06):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def birth(self):
        pass

    def eat(self):
        print("I'm eat only healthy food")


sarah = Woman('Sarah', 'Connor')

if __name__ == "__main__":
    sarah.eat()
