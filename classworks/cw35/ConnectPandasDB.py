import matplotlib.pyplot as plt
import pandas as pd

# client = MongoClient('localhost', 27017)
# mydb = client['mydatabase']
# mycol = mydb['customers']
# cursor = mycol.find()
# list_cur = list(cursor)
# df = DataFrame(list_cur)
# df.plot(kind='scatter', x='name', y='address')
# print(df.head())
# plt.show()

read_apple = pd.read_csv('apple.csv')
new_sample_df = read_apple['Close']
print(new_sample_df)
new_sample_df.to_csv('new_apple.csv')
read_new_apple = pd.read_csv('new_apple.csv')['Close']
mean_close = read_new_apple.mean()
median_close = read_new_apple.median()
mode_close = read_new_apple.mode()[0]
for x in read_new_apple.index:
    if 99 < read_new_apple.loc[x] < 101:
        read_new_apple.loc[x] = None
print(read_new_apple.to_string())
print("Mean close is: ", mean_close)
print("Median close is: ", median_close)
print("Mode close is: ", mode_close)

# as inplace=True is NOT written, it doesn't change the read_new_apple values
with_median = read_new_apple.fillna(median_close)
print(with_median.to_string())

with_mode = read_new_apple.fillna(mode_close)
print(with_mode.to_string())

# as inplace=True is written, it changes the read_new_apple values
read_new_apple.fillna(mean_close, inplace=True)
print(read_new_apple.to_string())

read_new_apple.to_csv('new_apple.csv')
plt.hist(read_new_apple, rwidth=0.9)
plt.title('APPLE Stock Close Prices from 2/23/2012 to 2/22/2017', size=12, fontweight="bold")
plt.xticks(style='italic')
plt.yticks(style='italic')
plt.xlabel('Frequency', fontweight="bold")
plt.ylabel('USD', fontweight="bold").set_rotation(0)

plt.axvline(mean_close, color='red', linestyle='dashed', linewidth=2)
plt.text(mean_close * 1.1, plt.ylim()[1] * 0.9, 'Mean: {:.4f}'.format(mean_close), color='red', style='italic')
plt.grid(alpha=0.35)
plt.show()

plt.subplot(2, 2, 1)
plt.title("With mean")
plt.plot(read_new_apple)
plt.subplot(2, 2, 2)
plt.title("With mode")
plt.plot(with_mode)
plt.subplot(2, 2, 3)
plt.title("With median")
plt.plot(with_median)
plt.show()
