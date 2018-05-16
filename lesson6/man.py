from lesson6.inheritance import Human06


class Man(Human06):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def fight(self, weapon):
        pass

    def eat(self):
        print("I'm eat unhealthy food")


john = Man('John', 'Connor')

if __name__ == '__main__':
    john.eat()
