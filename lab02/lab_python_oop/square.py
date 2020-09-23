from lab_python_oop.color import FigureColor
from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):

    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, side, color):
        self.side = side
        self.fc = FigureColor()
        self.fc.colorproperty = color

    def square(self):
        return self.side * self.side

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_figure_type(),
            self.fc.colorproperty,
            self.side,
            self.square()
        )
