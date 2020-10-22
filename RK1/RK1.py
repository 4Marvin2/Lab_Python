# вариант запроса Д
# вариант предметной области 18 : музыкальное произведение - оркестр
from operator import itemgetter


class Composition:
    # музыкальная композиция
    def __init__(self, id, title, listeners, orchestra_id):
        self.id = id
        self.title = title
        self.listeners = listeners
        self.orchestra_id = orchestra_id


class Orchestra:
    # оркестр
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CompOrch:
    # композиции оркестра для реализации связи
    # многие-ко-многим
    def __init__(self,  orch_id, comp_id):
        self.orch_id = orch_id
        self.comp_id = comp_id

# оркестры
orchs = [
    Orchestra(1, "Royal Concertgebouw Orchestra"),
    Orchestra(2, "Berlin Philharmonic Orchestra"),
    Orchestra(3, "Vienna Philharmonic Orchestra"),

    Orchestra(4, "London Symphony Orchestra"),
    Orchestra(5, "Chicago Symphony Orchestra"),
    Orchestra(6, "Cleveland Orchestra")
]

# музыкальные композиции
comps = [
    Composition(1, "Sun Valley Serenade", 10000, 1),
    Composition(2, "Toccata", 22000, 2),
    Composition(3, "Love is blue", 45500, 2),
    Composition(4, "Peer Gynt, Op. 23", 52000, 3),
    Composition(5, "Eine kleine Nachtmusik, K.525: I. Allegro", 15000, 3),
    Composition(6, "Symphony No.40 in G Minor, K.550: II. Andante", 100000, 3),
    Composition(7, "Eine kleine Nachtmusik, K.525: IV. Rondo: Allegro", 10400, 3)
]

comps_orchs = [
    CompOrch(1, 1),
    CompOrch(2, 2),
    CompOrch(2, 3),
    CompOrch(3, 4),
    CompOrch(3, 5),
    CompOrch(3, 6),
    CompOrch(3, 7),

    CompOrch(4, 1),
    CompOrch(5, 2),
    CompOrch(5, 3),
    CompOrch(6, 4),
    CompOrch(6, 5),
    CompOrch(6, 6),
    CompOrch(6, 7),
]

def main():
    # соединение данных один-ко-многим
    one_to_many = [(c.title, c.listeners, o.name)
                   for o in orchs
                   for c in comps
                   if c.orchestra_id == o.id]

    # соединение данных многие-ко-многим
    many_to_many_temp = [(o.name, co.orch_id, co.comp_id)
                         for o in orchs
                         for co in comps_orchs
                         if o.id == co.orch_id]

    many_to_many = [(c.title, c.listeners, orch_name)
                    for orch_name, orch_id, comp_id in many_to_many_temp
                    for c in comps if c.id == comp_id]

    print('Задание Д1')
    res1 = []
    for i in one_to_many:
        if i[0][-2:] == "ro":
            res1.append(i[0:3:2])
    print(res1)

    print('\nЗадание Д2')
    res2_unsorted = []
    for o in orchs:
        o_comps = list(filter(lambda i: i[2] == o.name, one_to_many))
        if len(o_comps) > 0:
            o_listeners = [listeners for _, listeners, _ in o_comps]
            o_listeners_sum = sum(o_listeners)
            o_listeners_count = len(o_listeners)
            o_listeners_average = o_listeners_sum / o_listeners_count
            res2_unsorted.append((o.name, int(o_listeners_average)))
    res2 = sorted(res2_unsorted, key=itemgetter(1), reverse=True)
    print(res2)

    print('\nЗадание Д3')
    res3 = {}
    for o in orchs:
        if o.name[0] == "C":
            o_comps = list(filter(lambda i: i[2] == o.name, many_to_many))
            o_comps_titles = [x for x, _, _ in o_comps]
            res3[o.name] = o_comps_titles
    print(res3)


if __name__ == '__main__':
    main()
