from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy


def main():
    my_rectangle = Rectangle(17, 17, "синего")
    my_circle = Circle(17, "зеленого")
    my_square = Square(17, "красного")

    print(my_rectangle)
    print(my_circle)
    print(my_square)

    my_array = numpy.array([[1, 2, 3], [4, 5, 6]], float)
    print("Метод внешнего пакета NumPy (shape) ", my_array.shape)


if __name__ == "__main__":
    main()
