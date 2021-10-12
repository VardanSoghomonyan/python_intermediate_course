class Parent:
    def __init__(self):
        print("Parent init")

    def method(self):
        print("Parent method")


class Child(Parent):
    def __init__(self):
        print("Child init")

    def method(self):
        print("Child method")


class Grandchild(Child):
    def __init__(self):
        super().__init__()
        print("Grandchild init and exit from constructor\n")

    def method(self):
        super(Child, self).method()


grandchild = Grandchild()
grandchild.method()
