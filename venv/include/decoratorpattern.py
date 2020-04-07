from abc import ABC, abstractmethod


class Creature(ABC):

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass


class Animal(Creature):

    def feed(self):
        print("I eat grass")

    def move(self):
        print("I walk forward")

    def make_noise(self):
        print("Wooo!")


class AbstractDecorator(Creature):

    def __init__(self, base):
        self.base = base

    def move(self):
        self.base.move()

    def feed(self):
        self.base.feed()

    def make_noise(self):
        self.base.make_noise()


class Swimming(AbstractDecorator):

    def move(self):
        print("I swim forward")

    def make_noise(self):
        print("...")


class Predator(AbstractDecorator):

    def feed(self):
        print("I eat other animals")


class Fast(AbstractDecorator):

    def move(self):
        self.base.move()
        print("Fast!")


animal = Animal()
animal.move()
animal.feed()
animal.make_noise()

swimming = Swimming(animal)
swimming.move()
swimming.feed()
swimming.make_noise()

predator = Predator(swimming)
predator.move()
predator.feed()
predator.make_noise()

fast = Fast(predator)
fast.move()
fast.feed()
fast.make_noise()

# наложение декоратора
faster = Fast(fast)
faster.move()
faster.feed()
faster.make_noise()

# снятие декоратора
print(faster.base)
faster.base = faster.base.base.base
print(faster.base)
faster.move()
faster.feed()
faster.make_noise()
