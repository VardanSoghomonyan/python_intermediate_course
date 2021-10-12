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


obj = Class4()
obj.print()

print("\nCalling parent class method with child object")
Class3.print(obj)
Class2.print(obj)
Class1.print(obj)
print("\nCalling parent class method from parent object")
Class3().print()
Class2().print()
Class1().print()
