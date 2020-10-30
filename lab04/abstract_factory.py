# порождающий паттерн проектирования
# абстрактная фабрика
# предметная область: кроссплатформенные элементы интерфейса,
#                     удовлетворяющие ОС Windows, Mac, Linux


from abc import ABC, abstractmethod


def define_resolution(platform):
    if platform == "Настольный ПК":
        return "2560x1600"
    elif platform == "Ноутбук":
        return "1600x1200"
    elif platform == "Смартфон":
        return "1280x1024"


# абстрактный класс окна с абстрактным методом его отрисовки
class Window(ABC):

    @abstractmethod
    def paint(self, resolution):
        pass


# абстрактный класс кнопки с абстрактным методом ее отрисовки
class Button(ABC):

    @abstractmethod
    def paint(self):
        pass


# абстрактный класс чек-бокса с абстрактным методом его отрисовки
class Checkbox(ABC):

    @abstractmethod
    def paint(self):
        pass

    @abstractmethod
    def paint_with_button(self, button):
        pass


# абстрактный класс текстового поля с абстрактным методом его отрисовки
class Textfield(ABC):

    @abstractmethod
    def paint(self):
        pass


# Абстрактная фабрика
class GUIFactory(ABC):

    @abstractmethod
    def create_window(self):
        pass

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

    @abstractmethod
    def create_textfield(self):
        pass


# класс окна для Windows
class WinWindow(Window):

    def paint(self, resolution):
        return f"Создание и отрисовка окна с разрешением {resolution} в стиле Windows"


# класс окна для macOS
class MacWindow(Window):

    def paint(self, resolution):
        return f"Создание и отрисовка окна с разрешением {resolution} в стиле macOS"


# класс окна для Linux
class LinuxWindow(Window):

    def paint(self, resolution):
        return f"Создание и отрисовка окна с разрешением {resolution} в стиле Linux"


# класс кнопки для Windows
class WinButton(Button):

    def paint(self):
        return "Отрисовка кнопки в стиле Windows"


# класс кнопки для macOS
class MacButton(Button):

    def paint(self):
        return "Отрисовка кнопки в стиле macOS"


# класс кнопки для Linux
class LinuxButton(Button):

    def paint(self):
        return "Отрисовка кнопки в стиле Linux"


# класс чек-бокса для Windows
class WinCheckbox(Checkbox):

    def paint(self):
        return "Отрисовка чек-бокса в стиле Windows"

    def paint_with_button(self, button):
        if type(button) == WinButton:
            result = button.paint()
            return f"Отрисовка чек-бокса и {result}"
        else:
            raise ValueError


# класс чек-бокса для macOS
class MacCheckbox(Checkbox):

    def paint(self):
        return "Отрисовка чек-бокса в стиле macOS"

    def paint_with_button(self, button):
        if type(button) == MacButton:
            result = button.paint()
            return f"Отрисовка чек-бокса и {result}"
        else:
            raise ValueError


# класс чек-бокса для Linux
class LinuxCheckbox(Checkbox):

    def paint(self):
        return "Отрисовка чек-бокса в стиле Linux"

    def paint_with_button(self, button):
        if type(button) == LinuxButton:
            result = button.paint()
            return f"Отрисовка чек-бокса и {result}"
        else:
            raise ValueError


# класс текстового поля для Windows
class WinTextfield(Textfield):

    def paint(self):
        return "Отрисовка текстового поля в стиле Windows"


# класс текстового поля для macOS
class MacTextfield(Textfield):

    def paint(self):
        return "Отрисовка текстового поля в стиле macOS"


# класс текстового поля для Linux
class LinuxTextfield(Textfield):

    def paint(self):
        return "Отрисовка текстового поля в стиле Linux"


# фабрика для Windows
class WinFactory(GUIFactory):

    def create_window(self):
        return WinWindow()

    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()

    def create_textfield(self):
        return WinTextfield()


# фабрика для macOS
class MacFactory(GUIFactory):

    def create_window(self):
        return MacWindow()

    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

    def create_textfield(self):
        return MacTextfield()


# фабрика для Linux
class LinuxFactory(GUIFactory):

    def create_window(self):
        return LinuxWindow()

    def create_button(self):
        return LinuxButton()

    def create_checkbox(self):
        return LinuxCheckbox()

    def create_textfield(self):
        return LinuxTextfield()


# клиентский код
def client_code(factory):

    window = factory.create_window()
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    textfield = factory.create_textfield()

    print(window.paint(define_resolution("Настольный ПК")))
    print(window.paint(define_resolution("Ноутбук")))
    print(window.paint(define_resolution("Смартфон")))
    print(button.paint())
    print(checkbox.paint())
    print(textfield.paint())
    print(checkbox.paint_with_button(button))


if __name__ == "__main__":

    print("Клиентский код на Windows")
    client_code(WinFactory())

    print('\n')

    print("Клиентский код на macOS")
    client_code(MacFactory())

    print('\n')

    print("Клиентский код на Linux")
    client_code(LinuxFactory())
