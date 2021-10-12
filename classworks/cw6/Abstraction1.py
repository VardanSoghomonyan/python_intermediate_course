from abc import ABC


class Polygon(ABC):
    def number_of_sides(self):
        raise Exception("You should define the number_of_sides method")


class Triangle(Polygon):
    # overriding abstract method
    def number_of_sides(self):
        print("I have 3 sides")


class Rectangle(Polygon):
    # overriding abstract method
    def number_of_sides(self):
        print("I have 4 sides")


class Pentagon(Polygon):
    # def number_of_sides(self):
    #     pass
    pass


triangle = Triangle()
rectangle = Rectangle()
pentagon = Pentagon()
triangle.number_of_sides()
rectangle.number_of_sides()
pentagon.number_of_sides()
