import abc
from abc import ABC


class Parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "Parent Class"


class Child(Parent):
    @property
    def geeks(self):
        return "Child Class"


try:
    r = Parent()
    print(r.geeks)
except Exception as err:
    print(err)

r = Child()
print(r.geeks)
