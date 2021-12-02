import pandas as pd

my_data = {'cars': ['BMW', 'Mercedes', 'Audi'],
           'passengers': [2, 7, None],
           'boolean': 'yes'}

data_frame = pd.DataFrame(my_data)
print("Dataframe: \n", data_frame)
print()

print("Dataframe loc[0]: \n", data_frame.loc[0])
print()

print("Dataframe loc[[0, 1]]: \n", data_frame.loc[[0, 1]])
print()

myvar1 = pd.DataFrame(my_data, index=['DAY1', 'DAY2', 'DAY3'])
print("DataFrame index: \n", myvar1)
print()

print("DataFrame loc['DAY2']: \n", myvar1.loc['DAY2'])
print()

print("DataFrame loc[['DAY2']]: \n", myvar1.loc[['DAY2']])
print()

my_data1 = [5, 9, 1]
print("Series my_data1: \n", pd.Series(my_data1))
print()

print("Series (my_data)[1]: \n", pd.Series(my_data)[1])
print()

myvar = pd.Series(my_data1, index=['x', 'y', 'z'])
print("Series index: \n", myvar)
print()

calories = {'day1': 500, 'day2': 250, 'day3': 0}
print("Series calories:\n", pd.Series(calories))
print()

print("Series calories with index:\n", pd.Series(calories, index=['day1', 'day2']))
print()
