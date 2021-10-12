class Person:
    def __init__(self, age=27, name="Person"):
        self.__age = age
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(18, 65):
            self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) in range(2, 20):
            self.__name = name


class Employee:
    __salary = 200000
    __company = "Company"

    def __init__(self, salary, company):
        self.__salary = salary
        self.__company = company

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary in range(50000, 1000000):
            self.__salary = salary

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company):
        if len(company) in range(2, 20):
            self.__company = company


class Teacher(Person, Employee):
    def __init__(self, age, name, salary, company, pay=0):
        Person.__init__(self, age, name)
        Employee.__init__(self, salary, company)
        self.__pay = pay

    def salary_statement(self):
        return self.salary + self.__pay

    def info(self):
        return f"Teacher info is the following:\nage is: {self.age}\nname is: {self.name}\nsalary is: {self.salary}\n" \
               f"company is: {self.company}"

    def report(self):
        write_file = open("TeacherInfo.txt", "w")
        write_file.write(self.info())
        write_file.close()

    @staticmethod
    def read():
        read_file = open("TeacherInfo.txt")
        s = read_file.read()
        read_file.close()
        return s


teacher = Teacher(30, "Anun", 250000, "Google")
print(teacher.info())
teacher.report()
print(teacher.read())

# haytararel shape class, ira hamar attribute lini koxm@, sahmanaum enq ira hamar makeres u paragic methodnet
# iranic jarang qarakusi, uxxankyuin, erankyuni, klor
# bolor attributner@ private lini, u getter setterov lini sax, vonc vor es xndir@
