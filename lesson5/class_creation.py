class Human(object):
    head = 1
    body = 1
    legs = 2
    arms = 2

    def eat(self, dish):
        print("I eat {}".format(dish))

    def sleep(self, dream):
        print('I am sleeping {}'.format(dream))

    def run(self, speed):
        print('I am running {}'.format(speed))


linda = Human()

if __name__ == '__main__':
    linda.eat('Fish')
    linda.sleep('Nightmare')
    linda.run('Slowly')
