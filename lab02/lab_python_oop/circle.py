from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
from math import pi


class Circle(Figure):

    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, radios, color):
        self.radios = radios
        self.fc = FigureColor()
        self.fc.colorproperty = color

    def square(self):
        return pi * self.radios * self.radios

    def __repr__(self):
        return '{} {} цвета с радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.fc.colorproperty,
            self.radios,
            self.square()
        )
