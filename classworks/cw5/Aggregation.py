class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return "Total " + str(self.pay.get_total() + self.bonus)


salary = Salary(100)
employee = Employee(salary, 10)
print(employee.annual_salary())
print()

# nuyn ban@ karox enq ayspes grel
employee = Employee(Salary(100), 10)
print(employee.annual_salary())
