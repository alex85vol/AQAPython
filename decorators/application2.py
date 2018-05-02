def application_template(application_text):
    return "Директору ТзОВ “Роги і Копита“\n Скоробагатьку П. С. \n Заява \n{0}".format(application_text)


def application_constructor(func):
    def app_wrapper(application_text):
        return func(application_text)

    return app_wrapper


vacation_text = "Прошу надати мені відпустку на 100 років"

emergency_text = "Прошу надати мені лікарняний на 1 день"

quit_text = "Прошу звільнити мене сьогоднішним числом"


@application_constructor
def vacation(application_text):
    vacation_app = application_constructor(application_template)
    return vacation_app(application_text)


@application_constructor
def emergency(application_text):
    emergency_app = application_constructor(application_template)
    return emergency_app(application_text)


@application_constructor
def fire(application_text):
    fire_app = application_constructor(application_template)
    return fire_app(application_text)


def main():
    choice = input("Вас вітає програма формування заяви."
                   " \n Якщо ви бажаєте сформувати заяву на відпустку натсиніть 1"
                   "\n Якщо ви бажаєте сформувати заяву про лікарняний натсиніть 2"
                   "\n Якщо ви бажаєте сформувати заяву на звільнення натсиніть 3"
                   "\n Зробіть ваш вибір: ")
    if choice == "1":
        print(vacation(vacation_text))
    elif choice == "2":
        print(emergency(emergency_text))
    elif choice == "3":
        print(fire(quit_text))
    else:
        print("There are no such option :" + choice)
        return main()


if __name__ == "__main__":
    main()
