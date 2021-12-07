import matplotlib.pyplot as plt
import pandas as pd

# creates plot of the given data and shows it by show() function
read_apple = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)
new_sample_df = read_apple.loc['2012-Feb', 'Close']
new_sample_df.plot()
plt.show()

# creates plot of the given data and shows it by show() function
read_data = pd.read_csv('data.csv')
read_data.plot()
plt.show()

read_data.plot(kind='scatter', x='Duration', y='Calories')
plt.show()

read_data['Pulse'].plot(kind='hist')
plt.show()
read_data['Duration'].plot(kind='hist')
plt.show()
