from abc import ABC


class A(ABC):
    def function(self):
        print("A Class")


class B(A):
    def function(self):
        print("B Class")


a = A()
a.function()
b = B()
b.function()
