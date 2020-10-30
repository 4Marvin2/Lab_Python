# структурный паттерн проектирования
# адаптер
# предметная область: клиент с помощью исходного интерфейса может проверить,
#                     подойдет ли цилиндрическая деталь к круглому отверстию.
#                     Появилась возможость обтачивать края параллелипипедной детали до цилиндрической.
#                     Для проверки подойдет ли параллелипипедная деталь к круглому отверстию
#                     необходимо использовать адаптер.


# класс цилиндрических деталей
class RoundDetail:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius


# класс параллелипипедных деталей
class SquareDetail:

    def __init__(self, width):
        self.width = width

    # для тестирования
    # def get_radius(self):
    #     return self.width

    def get_width(self):
        return self.width


# класс круглых отверстий
class RoundHole:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def fits(self, round_detail):

        if self.get_radius() == round_detail.get_radius():
            return f"Деталь подходит. " \
                   f"Радиус детали: {round_detail.get_radius()}, радиус отверстия {self.get_radius()}"
        else:
            return f"Деталь не подходит. " \
                   f"Радиус детали: {round_detail.get_radius()}, радиус отверстия {self.get_radius()}"


# адаптер
class SquareDetailAdapter(RoundDetail):

    def __init__(self, square_detail):
        self.square_detail = square_detail

    def get_radius(self):
        return self.square_detail.get_width() / 2


def client_code():
    hole = RoundHole(10)
    round_detail1 = RoundDetail(10)
    round_detail2 = RoundDetail(20)
    square_detail1 = SquareDetail(10)
    square_detail2 = SquareDetail(20)

    print("Проверяем цилиндрические детали:")
    print(hole.fits(round_detail1))
    print(hole.fits(round_detail2))
    # не работает, т.к. параллелипипедная деталь не соответсвует круглому отверстию
    # print(hole.fits(square_detail1))

    print('\n')

    print("Проверяем параллелипипедные детали")
    square_detail_adapter1 = SquareDetailAdapter(square_detail1)
    print(hole.fits(square_detail_adapter1))
    square_detail_adapter2 = SquareDetailAdapter(square_detail2)
    print(hole.fits(square_detail_adapter2))


if __name__ == "__main__":
    client_code()
