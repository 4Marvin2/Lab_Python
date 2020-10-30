# поведенческий паттерн проектирования
# наблюдатель
# предметная область: магазин одежды делает рассылку подписчикам, при поступлении нового товара


from abc import ABC, abstractmethod
from termcolor import colored


# абстрактный класс издателя
class Publisher(ABC):

    @abstractmethod
    def attach(self, subscriber):
        pass

    @abstractmethod
    def detach(self, subscriber):
        pass

    @abstractmethod
    def notify(self):
        pass


# абстрактный класс подписчика(наблюдателя)
class Subscriber(ABC):

    @abstractmethod
    def update(self, publisher):
        pass


# магазин, оповещающий подписчиков
class StorePublisher(Publisher):

    def __init__(self):
        self.new_goods = ''
        self.subscribers = []

    def attach(self, subscriber):
        self.subscribers.append(subscriber)
        return colored("Publisher:", 'red') + f"Добавлен новый подписчик с ником {subscriber.name}"

    def detach(self, subscriber):
        self.subscribers.remove(subscriber)
        return colored("Publisher:", 'red') + f"Удален подписчик с ником {subscriber.name}"

    def notify(self):
        print(colored("Publisher:", 'red'), "Оповещаю подписчиков...")
        subscribers_reacts = []
        for subscriber in self.subscribers:
            subscribers_reacts.append(subscriber.update(self))
        for react in subscribers_reacts:
            if react != 1:
                print(react)

    def goods_arrival(self, goods):
        self.new_goods = goods
        print(colored("Publisher:", 'red'), f"Поступил новый товар - {self.new_goods}")
        self.notify()


# Человек, подписавшиея на оповещения о поступлении кроссовок
class SneakersSubscriber(Subscriber):

    def __init__(self, name):
        self.name = name

    def update(self, publisher):
        if publisher.new_goods == "кроссовки":
            react = colored("SneakersSubscriber:", 'green') + f"{self.name} реагирует на новое поступление кроссовок"
            return react
        else:
            return 1


# Человек, подписавшиеся на оповещения о поступлении худи
class HoodiesSubscriber(Subscriber):

    def __init__(self, name):
        self.name = name

    def update(self, publisher):
        if publisher.new_goods == "худи":
            react = colored("SneakersSubscriber:", 'green') + f"{self.name} реагирует на новое поступление худи"
            return react
        else:
            return 1


def client_code():
    store = StorePublisher()

    first_sneakers_subscriber = SneakersSubscriber("James")
    print(store.attach(first_sneakers_subscriber))
    second_sneakers_subscriber = SneakersSubscriber("Emma")
    print(store.attach(second_sneakers_subscriber))
    first_hoodies_subscriber = HoodiesSubscriber("Oliver")
    print(store.attach(first_hoodies_subscriber))

    print('\n')

    store.goods_arrival("кроссовки")
    store.goods_arrival("худи")

    print('\n')

    print(store.detach(first_sneakers_subscriber))

    print('\n')

    store.goods_arrival("кроссовки")


if __name__ == "__main__":
    client_code()
