import sys


# get path to data-file
path = sys.argv[1]

# get in/out time from file
with open(path, 'r') as d_file:
	#in_out_time = [[j for j in i.split(' ')] for i in d_file]
	in_out_time = [j.rstrip() for i in d_file for j in i.split(' ')]

# save people moving to dict
step = 1
move_people = {}
for i in in_out_time:
	if move_people.get(i) is None:
		move_people[i] = step
	else:
		move_people[i] += step
	step *= -1

# count the number people inside (for sorted time)
number_people = [[i, move_people[i]] for i in move_people]
number_people.sort()
for i in range(1, len(number_people)):
	number_people[i][1] += number_people[i-1][1]

# delete immutable time segments
i = 1 - len(number_people)
while i != 0:
	if number_people[i][1] == number_people[i-1][1]:
		number_people.pop(i)	
	i += 1

# output time segment(s) of max people	
time_arr = [i[0] for i in number_people]
count_arr = [i[1] for i in number_people]
max_people = max(count_arr)
start_ = 0
while max_people in count_arr:
	ind_max = count_arr.index(max_people, start_)
	print(f'{time_arr[ind_max]} {time_arr[ind_max+1]}')
	count_arr[ind_max] = -1
	start = ind_max
