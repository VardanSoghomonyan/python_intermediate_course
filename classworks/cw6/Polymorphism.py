class Mammal:
    def move(self):
        print("Mammal moves")


class Child(Mammal):
    def move(self):
        print("Child moves")


mammal = Mammal()
mammal.move()
child = Child()
child.move()
