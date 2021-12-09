import matplotlib.pyplot as plt
import numpy as np
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

x_points = np.asarray([0, 6])
y_points = np.asarray([0, 10])
# shows linear graph
plt.plot(x_points, y_points)
plt.show()
# shows only first and last points 'o'
plt.plot(x_points, y_points, 'o')
plt.show()

x_points = np.asarray([1, 2, 6, 9])
y_points = np.asarray([3, 1, 5, 4])
# shows linear graph by provided points
plt.plot(x_points, y_points)
plt.show()

points = np.asarray([3, 1, 5, 4, 9, 1])
points_x = np.asarray([2, 4, 3, 1, 7, 1])
points1 = np.asarray([0, 9, 5, 6, 2, 5])
points1_x = np.asarray([0, 6, 5, 2, 4, 1])
# if only one array is given, it is automatically considered as points of y axis. Points of x axis are integers
plt.plot(points, marker='*')
plt.plot(points)
plt.show()

plt.plot(points, 'o:r')
plt.show()

# define marker size and its border color
plt.plot(points, marker='o', markersize=20, mec='r')
plt.show()

# define marker size and its color
plt.plot(points, marker='o', markersize=20, mfc='r')
plt.show()

# define marker size, its color, its color, graph line style, graph line color, graph line width
plt.plot(points, marker='o', markersize=20, mfc='#4CAF50', mec='red', linestyle='dotted', color='black', linewidth=5)
plt.plot(points1, marker='*', markersize=15, mfc='#4CAF50', mec='blue', linestyle='dotted', color='purple',
         linewidth=10)
plt.show()

# plot 2 graphs on the same chart
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'red', 'size': 15}
plt.plot(points, points_x, points1, points1_x)
plt.xlabel('Values', fontdict=font2)
plt.ylabel('Points', fontdict=font2)
plt.title('Average value of points', fontdict=font1)
plt.show()