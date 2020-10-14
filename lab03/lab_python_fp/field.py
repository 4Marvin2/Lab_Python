goods = [
    {'title': 'Ковер', 'price': '2000', 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': '5300', 'color': 'black'},
    {'title': 'Кровать', 'price': '10500', 'color': 'white'}
]


def field(items, *args):
    assert len(args) > 0, 'Не переданы аргументы полей словаря'
    if len(args) == 1:
        for i in range(len(items)):
            if args[0] in items[i] and items[i].get(args[0]) is not None:
                yield items[i].get(args[0])
    else:
        for i in range(len(items)):
            s = {}
            for j in range(len(args)):
                if args[j] in items[i] and items[i].get(args[j]) is not None:
                    s.update({args[j]: items[i].get(args[j])})
            yield s


def main():
    f = field(goods, 'title')
    for i in f:
        print(i, end=', ')
    print('\n', end='')
    f = field(goods, 'title', 'price')
    for i in f:
        print(i, end=', ')


if __name__ == "__main__":
    main()
