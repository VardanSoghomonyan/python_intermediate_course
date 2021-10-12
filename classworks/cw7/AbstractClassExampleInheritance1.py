from abc import ABC, abstractmethod


class AbstractClassExample(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass


class Add(AbstractClassExample):
    def do_something(self):
        return self.value + 42


class Multiple(AbstractClassExample):
    def do_something(self):
        return self.value * 42


a = Add(5)
b = Multiple(4)
print(a.do_something())
print(b.do_something())
