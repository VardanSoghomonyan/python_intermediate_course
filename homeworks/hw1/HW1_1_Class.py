class Employee:
    firstname = None
    lastname = None
    age = None
    time = None
    salary = None
    salaryRate = None

    def __init__(self, firstname, lastname, age, time, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.time = time
        self.salary = salary

    def info(self):
        print("Employee: \n firstname is {}\n lastname is {}\n age is {}\n time is {}\n salary is {}\n"
              .format(self.firstname, self.lastname, self.age, self.time, self.salary))

    def givebonus(self):
        if self.time > 8:
            self.salaryRate = 8 * self.time
            self.salary += self.salaryRate
            return True


class Manager(Employee):
    pass


class SalesPerson(Employee):
    numberOfSales = 1
    # salary = None
    salesPersonSalary = None

    def __init__(self, firstname, lastname, age, time, salary, numberOfSales):
        super().__init__(firstname, lastname, age, time, salary)
        # self.salary = salary
        self.salesPersonSalary = salary
        self.numberOfSales = numberOfSales

    def givebonus(self):
        if super().givebonus():
            # if I activate the below comment, get unclear output. Would like to discuss
            # self.salary += self.salaryRate * self.numberOfSales
            self.salesPersonSalary += self.salaryRate * self.numberOfSales


employee = Employee("Armen", "Employee", 35, 9, 200000)
employee.info()
employee.givebonus()
print("Employee salary is: ", employee.salary)
print()

salesperson = SalesPerson("Sales", "Person", 35, 9, 200000, 3)
salesperson.info()
salesperson.givebonus()
# if I activate the below comment, get unclear output. Would like to discuss
# print(f"Salesperson salary is: {salesperson.salary}")
print(f"Salesperson salary is: {salesperson.salesPersonSalary}")
