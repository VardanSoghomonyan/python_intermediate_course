import pandas as pd

readCSV = pd.read_csv('dirtydata.csv')

# dropna() function removes invalid data and created temporary data for processing, without changing the original data
new_readCSV = readCSV.dropna()
print('readCSV.dropna().to_string() is:\n', new_readCSV.to_string())
print()

# dropna(inplace=True) changes the original file but doesn't save automatically
readCSV.dropna(inplace=True)
print('readCSV.dropna(inplace=True)', readCSV.to_string())

# fillna(inplace=True) changes the original file by filling NULLs with provided value (130) but doesn't save automatically
readCSV.fillna(130, inplace=True)
print('readCSV.fillna(130, inplace=True)', readCSV.to_string())

# readCSV['Calories'].fillna(inplace=True) changes the original file by filling NULLs with provided value (130)
# only for the mentioned column but doesn't save automatically
readCSV['Calories'].fillna(130, inplace=True)
print('readCSV["Calories"].fillna(130, inplace=True)', readCSV.to_string())

readCSV['Calories'].fillna(readCSV['Calories'].mean(), inplace=True)
print("readCSV['Calories'].fillna((readCSV[Calories].mean(), inplace=True)", readCSV.to_string())
