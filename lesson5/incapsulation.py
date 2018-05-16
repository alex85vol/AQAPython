class IncapsulationClass(object):
    def __init__(self, a, b):
        self.__a = a
        self.b = b

    def __hidden(self):
        return 1


inc_instance = IncapsulationClass(1, 2)

if __name__ == "__main__":
    # inc_instance.__a
    print(inc_instance.b)
    #inc_instance.__hidden()
