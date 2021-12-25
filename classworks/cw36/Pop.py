import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(4, 2), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]], columns=['data1', 'data2'])
print("df is:\n", df)

index = [('California', 2000),
         ('California', 2010),
         ('Texas', 2000),
         ('Texas', 2010),
         ('New York', 2000),
         ('New York', 2010)]
populations = [33871648, 37253956, 20851820, 25145561, 18976457, 19378102]
pop = pd.Series(populations, index=index)
print('pop is:\n', pop)

data = {('California', 2000): 33871648,
        ('California', 2010): 37253956,
        ('Texas', 2000): 20851820,
        ('Texas', 2010): 25145561,
        ('New York', 2000): 18976457,
        ('New York', 2010): 19378102
        }
print('pd.Series(data) is:\n', pd.Series(data))

print('pd.MultiIndex.from_arrays:\n', pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]]))

print('pd.MultiIndex.from_tuples:\n', pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)]))

print('pd.MultiIndex.from_product:\n', pd.MultiIndex.from_product([['a', 'b'], [1, 2]]))

index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]], names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']], names=['subject', 'type'])
data = np.round(np.random.rand(4, 6), 1)
data[:, ::2] *= 10
data += 37
health_data = pd.DataFrame(data, index=index, columns=columns)
print('health_data is:\n', health_data)
print("health_data['Guido', 'HR'] is:\n", health_data['Guido', 'HR'])
print('health_data.iloc[:2,:2] is:\n', health_data.iloc[:2, :2])
print("health_data.loc[:, ('Bob', 'HR')] is:\n", health_data.loc[:, ('Bob', 'HR')])

idx = pd.IndexSlice
print("health_data.loc[idx[:, 1], idx[:, 'HR']] is:\n", health_data.loc[idx[:, 1], idx[:, 'HR']])

index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]])
data = pd.Series(np.random.rand(6), index=index)
data.index.names = ['char', 'int']
print("data is:\n", data)
print("data.sort_index() is:\n", data.sort_index())

pop_flat = pop.reset_index(name='populations')
print("pop_flat is:\n", pop_flat)

# pop_flat.set_index(['state', 'year'])
# print("pop_flat.set_index(['state', 'year']) is:\n", pop_flat.set_index(['state', 'year']))

print("health_data.mean(level='year') is:\n", health_data.mean(level='year'))
print("health_data.mean(axis=1, level='type') is:\n", health_data.mean(axis=1, level='type'))


def make_df(column, indexes):
    data_in_function = {c: [str(c) + str(i) for i in indexes]
                        for c in column}
    return pd.DataFrame(data_in_function, indexes)


print("make_df is:\n", make_df('ABC', range(3)))

ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
print("pd.concat(ser1, ser2) is:\n", pd.concat([ser1, ser2]))

df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
print("pd.concat([df1, df2]) is:\n", pd.concat([df1, df2]))
print("df1.append(df2) is:\n", df1.append(df2))

df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
print("pd.concat([df3, df4], axis='columns') is:\n", pd.concat([df3, df4], axis='columns'))

x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])
y.index = x.index
print("pd.concat([x, y]) is:\n", pd.concat([x, y]))
print("pd.concat([x, y], keys=['x', 'y']) is:\n", pd.concat([x, y], keys=['x', 'y']))

df5 = make_df('ABC', [1, 2])
df6 = make_df('BCD', [3, 4])
print("pd.concat([df5, df6]) is:\n", pd.concat([df5, df6]))
print("pd.concat([df5, df6], join='inner') is:\n", pd.concat([df5, df6], join='inner'))

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
print("pd.merge(df1, df2) is:\n", pd.merge(df1, df2))
