import math
import sys


def read_number():
    try:
        x = float(input())
    except:
        print('Неверный символ, повторите ввод: ')
        return read_number()
    return x


print('Попов М. А. ИУ5-55Б')
if len(sys.argv) == 4:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except:
        print('Неверные параметры командной строки')
        exit()
# elif len(sys.argv) != 1:
    # print('Неверные параметры командной строки')
    # exit()
elif len(sys.argv) == 3:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    except:
        print('Неверные параметры командной строки')
        exit()
    print('Введите третий коэффициент: ')
    c = read_number()
elif len(sys.argv) == 2:
    try:
        a = float(sys.argv[1])
    except:
        print('Неверные параметры командной строки')
        exit()
    print('Введите второй коэффициент: ')
    b = read_number()
    print('Введите третий коэффициент: ')
    c = read_number()
else:
    print('Введите первый коэффициент: ')
    a = read_number()
    print('Введите второй коэффициент: ')
    b = read_number()
    print('Введите третий коэффициент: ')
    c = read_number()
D = b**2 - 4 * a * c
if (D > 0) and (a != 0):
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    if x1 > 0:
        print(math.sqrt(x1), -math.sqrt(x1), end=' ')
    elif x1 == 0:
        print(x1)
    if x2 > 0:
        print(math.sqrt(x2), -math.sqrt(x2))
    elif x2 == 0:
        print(x2)
    if (x1 < 0) and (x2 < 0):
        print('Корней нет')
elif (D > 0) and (a == 0):
    x = -c / b
    if x > 0:
        print(math.sqrt(x), -math.sqrt(x))
    elif x == 0:
        print(-x)
    else:
        print('Корней нет')
elif (D == 0) and (a == 0) and (c == 0):
    print('Корней бесконечно много')
else:
    print('Корней нет')
