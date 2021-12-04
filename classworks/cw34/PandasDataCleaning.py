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
print("readCSV['Calories'].fillna((readCSV[Calories].mean(), inplace=True)\n", readCSV.to_string())

readCSV['Date'] = pd.to_datetime(readCSV['Date'])
readCSV.dropna(subset=['Date'], inplace=True)
print("readCSV.dropna(subset=['Date'], inplace=True)\n", readCSV.to_string())

# this changes the specified cell
readCSV.loc[7, 'Duration'] = 45
print("readCSV.loc[7, 'Duration']\n", readCSV.to_string())

# this changes the all cells that not meet the condition
for x in readCSV.index:
    if readCSV.loc[x, 'Duration'] > 120:
        readCSV.loc[x, 'Duration'] = 120
print("readCSV.loc[7, 'Duration'] to the specified value\n", readCSV.to_string())

for x in readCSV.index:
    if readCSV.loc[x, 'Duration'] > 120:
        readCSV.drop(x, inplace=True)
print("readCSV.drop(x, inplace=True)\n", readCSV.to_string())

# returns True for the duplicated row in the data
print("readCSV.duplicated()\n", readCSV.duplicated())

# removes duplicated rows of the data, but not from the original data
readCSV.drop_duplicates(inplace=True)
print("readCSV.drop_duplicates(inplace=True)\n", readCSV.to_string())

# this method used to write the data to file
created_data = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Armenia', 'Artsakh'],
    'population': [17.4, 143.5, 3, 0.15],
    'square': [22958456, 156874598, 30000, 100000]
})
print("created_data\n", created_data)
created_data.to_csv('Country.csv')

titanic_df = pd.read_csv('titanic.csv')
print("titanic_df.head()\n", titanic_df.head().to_string())
print("titanic_df.groupby(['Sex', 'Survived'])['PassengerID'].count()\n",
      titanic_df.groupby(['Sex', 'Survived'])['PassengerID'].count())
print("titanic_df.groupby(['PClass', 'Survived'])['PassengerID'].count()\n",
      titanic_df.groupby(['PClass', 'Survived'])['PassengerID'].count())
titanic_pivot_Table = titanic_df.pivot_table(index=['Sex'], columns=['PClass'], values='Name', aggfunc='count')
print("titanic_pivot_Table.loc['female', ['1st', '2nd', '3rd']]\n",
      titanic_pivot_Table.loc['female', ['1st', '2nd', '3rd']])
