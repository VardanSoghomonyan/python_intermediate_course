class Class1:
    def print(self):
        print("In class 1")


class Class2(Class1):
    def print(self):
        print("In class 2")


class Class3(Class1):
    def print(self):
        print("In class 3")


class Class4(Class2, Class3):
    def print(self):
        print("In class 4")
        Class3.print(self)
        Class2.print(self)
        Class1.print(self)


obj = Class4()
obj.print()
