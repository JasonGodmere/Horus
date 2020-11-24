
import pandas as pd
import time
import matplotlib.pyplot as plt
import os

# testing pandas overhead for storing/retrieving csv files for EOH nodes
# from database rather than storing it explicitly in table in model
df = pd.DataFrame(columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10'])

for col in df.columns:
	df[col] = range(0, 1)

df.to_csv('csv_test.csv', header=False)

alt_df = df.copy()

def func(df, alt_df):
	return df.append(alt_df)


data = pd.DataFrame(columns=['to_csv_time', 'from_csv_time'])

sum_to = 0
sum_from = 0
sum_node = 0

for i in range(0, 8760):

	#df = func(df, alt_df)

	init = time.time()
	alt_df.to_csv('csv_test.csv', mode='a', header=False)
	to_csv_time = (time.time() - init) * 1000 # milliseconds


	init = time.time()
	val = pd.read_csv('csv_test.csv').iloc[-1, 0]
	from_csv_time = (time.time() - init) * 1000 # milliseconds

	df = pd.read_csv('csv_test.csv')

	row = len(df.index)
	col = len(df.columns)

	total_time = from_csv_time + to_csv_time

	file_size = round(os.path.getsize('csv_test.csv') / (1024 * 1024), 2)

	# assuming requests have to be served/recieved in < 3 seconds
	node_cap = 5000 / total_time

	delay = 50
	if i % delay == 0:
		sum_to += to_csv_time
		sum_from += from_csv_time
		sum_node += node_cap

		av_to = sum_to / delay
		av_from = sum_from / delay
		av_node = sum_node / delay
		print(f'Row/Col: {row} / {col} || Total: {round(av_to, 2)} / {round(av_from, 2)} || File Size: {file_size} MB || Node Capacity: {av_node}', end='\r')
		sum_to = 0
		sum_from = 0
		sum_node = 0
	else:
		sum_to += to_csv_time
		sum_from += from_csv_time
		sum_node += node_cap

	data.loc[i, 'to_csv_time'] = to_csv_time
	data.loc[i, 'from_csv_time'] = from_csv_time


data.plot()
plt.show()