class Address:
    def __init__(self, country, city, street, building):
        self.country = country
        self.city = city
        self.street = street
        self.building = building

    def address_info(self):
        print(
            f"The address in the following:\n country is: {self.country}\ncity is: {self.city}\n"
            f"street is: {self.street}\nbuilding is: {self.building}")


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        # self.address = address
        self.address = Address(address)

    def info(self):
        return print("Person is: ", self.name, self.age, self.address.address_info())


address = Address("Armenia", "Yerevan", "Abovyan street", "building 7")
person = Person("Vardan", 15, address)
print(person.info())
print()
