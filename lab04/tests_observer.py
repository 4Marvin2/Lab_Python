from unittest import TestCase
from termcolor import colored
from observer import SneakersSubscriber
from observer import HoodiesSubscriber
from observer import StorePublisher


class ObserverTestCase(TestCase):

    # проверка добавления нового подписчика
    def test_attach(self):
        sneakers_subscriber = SneakersSubscriber("Name1")
        hoodies_subscriber = HoodiesSubscriber("Name2")
        store = StorePublisher()

        store.attach(sneakers_subscriber)
        store.attach(hoodies_subscriber)

        self.assertEqual(type(sneakers_subscriber), type(store.subscribers[0]))
        self.assertEqual(type(hoodies_subscriber), type(store.subscribers[1]))

    # проверка удаления подписчика
    def test_detach(self):
        sneakers_subscriber = SneakersSubscriber("Name1")
        hoodies_subscriber = HoodiesSubscriber("Name2")
        store = StorePublisher()
        store.attach(sneakers_subscriber)
        store.attach(hoodies_subscriber)

        store.detach(sneakers_subscriber)

        self.assertEqual(1, len(store.subscribers))
        self.assertEqual(type(hoodies_subscriber), type(store.subscribers[0]))

    # проверка реакции на поступление новых кроссовок людей, подписанных на кроссовки
    def test_react_sneakers_subscriber(self):
        store = StorePublisher()
        sneakers_subscriber = SneakersSubscriber("Name1")
        store.new_goods = "кроссовки"
        self.assertEqual(colored("SneakersSubscriber:", 'green') +
                         f"{sneakers_subscriber.name} реагирует на новое поступление кроссовок",
                         sneakers_subscriber.update(store))

    # проверка реакции на поступление новых кроссовок людей, не подписанных на кроссовки
    def test_noreact_hoodies_subscriber(self):
        store = StorePublisher()
        hoodies_subscriber = HoodiesSubscriber("Name1")
        store.new_goods = "кроссовки"
        self.assertEqual(1, hoodies_subscriber.update(store))

    # проверка реакции на поступление новых худи людей, подписанных на худи
    def test_react_hoodies_subscriber(self):
        store = StorePublisher()
        hoodies_subscriber = HoodiesSubscriber("Name1")
        store.new_goods = "худи"
        self.assertEqual(colored("SneakersSubscriber:", 'green') +
                         f"{hoodies_subscriber.name} реагирует на новое поступление худи",
                         hoodies_subscriber.update(store))

    # проверка реакции на поступление новых худи людей, не подписанных на худи
    def test_noreact_sneakers_subscriber(self):
        store = StorePublisher()
        sneakers_subscriber = SneakersSubscriber("Name1")
        store.new_goods = "худи"
        self.assertEqual(1, sneakers_subscriber.update(store))
