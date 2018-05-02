def application_constructor(application_text):
    def application_template():
        return "Директору ТзОВ “Роги і Копита“\n Скоробагатьку П. С. \n Заява"

    return application_template() + application_text


def vacation_text():
    return "\n Прошу надати мені відпустку на 100 років"


def emergency_text():
    return "\n Прошу надати мені лікарняний на 1 день"


def quit_text():
    return "\n Прошу звільнити мене сьогоднішним числом"


def vacation():
    return application_constructor(vacation_text())


def emergency():
    return application_constructor(emergency_text())


def fire():
    return application_constructor(quit_text())


def application():
    choice = input("Вас вітає програма формування заяви."
                   " \n Якщо ви бажаєте сформувати заяву на відпустку натсиніть 1"
                   "\n Якщо ви бажаєте сформувати заяву про лікарняний натсиніть 2"
                   "\n Якщо ви бажаєте сформувати заяву на звільнення натсиніть 3"
                   "\n Зробіть ваш вибір: ")
    if choice == "1":
        print(vacation())
    elif choice == "2":
        print(emergency())
    elif choice == "3":
        print(fire())
    else:
        print("There are no such option :" + choice)
        return application()


application()
