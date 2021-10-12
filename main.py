# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from homeworks.hw1.HW1_1_Class import Employee


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    d = Employee("Armen", "Armenyan", 35, 9, 200000)
    d.info()
    print(d.salary)

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
