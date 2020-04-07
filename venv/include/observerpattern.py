# Паттерн Наблюдатель (Observer)
from abc import ABC, abstractmethod


class NotificationManager:
    # Наблюдаемая система = Абстрактный наблюдаемый объект

    def __init__(self):
        # При инициализации множество подписчиков задается пустым
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        # Отправка уведомления всем подписчикам
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    # Абстрактный наблюдатель

    @abstractmethod
    def update(self, message):
        pass


class MessageNotifier(AbstractObserver):

    def __init__(self, name):
        self.__name = name

    def update(self, message):
        print(f"{self.__name} received message!")


class MessagePrinter(AbstractObserver):

    def __init__(self, name):
        self.__name = name

    def update(self, message):
        print(f"{self.__name} received message: {message}")


notifier = MessageNotifier("Notifier1")
printer1 = MessagePrinter("Printer1")
printer2 = MessagePrinter("Printer2")

manager = NotificationManager()

manager.subscribe(notifier)
manager.subscribe(printer1)
manager.subscribe(printer2)

manager.notify("Hi!")
