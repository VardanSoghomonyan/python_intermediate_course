import time
from abc import ABC


class People(ABC):
    def skin_color(self):
        raise Exception("You should define the skin_color in {} class".format(self.__class__.__name__))

    def get_people_info(self, skin_color):
        print("I am {} and my skin color is {}\n".format(self.__class__.__name__, skin_color))


class European(People):
    # overriding abstract method
    def skin_color(self):
        super().get_people_info("white")


class African(People):
    # overriding abstract method
    def skin_color(self):
        super().get_people_info("black")


class Latino(People):
    pass


european = European()
african = African()
latino = Latino()
european.skin_color()
time.sleep(1)
african.skin_color()
time.sleep(1)
latino.skin_color()
