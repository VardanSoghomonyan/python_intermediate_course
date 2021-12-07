import pandas as pd

read_apple = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)
# if it is needed to calculate mean of the given column value for the provided exact month
print("read_apple.loc['2012-Feb', 'Close'].mean():\n", read_apple.loc['2012-Feb', 'Close'].mean())
print()

# if it is needed to calculate mean of the given column value for the provided time range
print("read_apple.loc['2015-Feb':'2012-Feb', 'Close'].mean():\n", read_apple.loc['2015-Feb':'2012-Feb', 'Close'].mean())
print()

# if it is needed to calculate mean of the given column value for the weeks ('W')
print("read_apple.resample('W')['Close'].mean():\n", read_apple.resample('W')['Close'].mean())
print()
