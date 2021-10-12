class Person:
    firstname = None
    lastname = None

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def display(self):
        print(type(self), "info is:")
        print(self.__dict__)
        print()


class Employee(Person):
    def __init__(self, firstname, lastname, company):
        super().__init__(firstname, lastname)
        self.company = company

    def display(self):
        print(
            f"Employee info is: \n firstname is {self.firstname}\n lastname is {self.lastname}\n company is {self.company}\n")


person = Person("Armen", "Employee")
person.display()

employee = Employee("Sales", "Person", "Google")
employee.display()
