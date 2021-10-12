class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    def display_info(self):
        print("Name: ", self.__name)


tom = Person("Tom")
tom.display_info()
tom.name = "Tommy"
tom.display_info()
del tom.name
