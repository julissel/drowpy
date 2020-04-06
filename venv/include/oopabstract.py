from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def do_something(self):
        print("Hi!")


class B(A):
    def do_something(self):
        print("Hello!")


obj = B()
obj.do_something()
