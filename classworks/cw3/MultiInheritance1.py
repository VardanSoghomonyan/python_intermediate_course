class Class1:
    def print(self):
        print("In class 1")


class Class2(Class1):
    pass


class Class3(Class1):
    def print(self):
        print("In class 3")


class Class4(Class2, Class3):
    pass


obj1 = Class4()
obj1.print()
