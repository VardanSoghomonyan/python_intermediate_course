import pandas as pd

readCSV = pd.read_csv('data.csv')
print('readCSV is:\n', readCSV)
print()
print('readCSV.to_string() is:\n', readCSV.to_string())
print()

# head() returns top rows
print('readCSV.head(10) is:\n', readCSV.head(10))
print()
print('readCSV.head() is:\n', readCSV.head())
print()

# tail() returns top rows
print('readCSV.tail(10) is:\n', readCSV.tail(10))
print()
print('readCSV.tail() is:\n', readCSV.tail())
print()
print('readCSV.info() is:\n', readCSV.info())
print()
print('readCSV.info is:\n', readCSV.info)
print()

# if number of rows >options.display.max_rows, then running print(df) it will print only first and last 5 rows, otherwise, all rows
print('default pd.options.display.max_rows is:\n', pd.options.display.max_rows)
print()
pd.options.display.max_rows = 80
print('changed pd.options.display.max_rows is:\n', pd.options.display.max_rows)
print()

readJSON = pd.read_csv('data.csv')
print('readJSON is:\n', readJSON)
print()
print('readJSON.to_string() is:\n', readJSON.to_string())
print()

dictionary_data = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127
    },
    "Calories": {
        "0": 409.1,
        "1": 479.0,
        "2": 340.0,
        "3": 282.4,
        "4": 406.0,
        "5": 300.5
    }
}

print('pd.DataFrame(dictionary_data) is:\n', pd.DataFrame(dictionary_data))
print()

# calculates and returns correlation
print("readCSV.corr()\n", readCSV.corr())
