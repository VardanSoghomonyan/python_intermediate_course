class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Unavailable age")

    @property
    def get_name(self):
        return self.__name

    def display_info(self):
        print("Name: ", self.__name, "\tAge: ", self.__age)


class Employee(Person):
    def details(self, company):
        print(self.get_name, " works in ", company)


tom = Employee("Tom", 40)
tom.display_info()
tom.age = 45
tom.display_info()
tom.age = -45
tom.display_info()
tom.details("Google")
