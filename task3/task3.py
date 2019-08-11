import sys

# get path to data-dir
dir_path = sys.argv[1]

# data from Cash*.txt to cash_arr[][]
cash_arr = []
for i in range(5):
	with open(f'{dir_path}Cash{i+1}.txt', 'r') as cash:
		cash_arr.append([float(j) for j in cash])

# array of sum`s for all Cash for each segment of time
ans_arr = [sum(i) for i in zip(cash_arr[0], cash_arr[1], cash_arr[2], cash_arr[3], cash_arr[4])]

print(ans_arr.index(max(ans_arr))+1)
