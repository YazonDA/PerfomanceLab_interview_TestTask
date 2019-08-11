import sys


# point position relative to 'square'
def pp_property(xy, square):
	#  if point in the VERTEX
	if xy in square:
		return 0
	# property lines/point check
	s = []
	for i in range(len(square)):
		suppose = for_edge(xy, [square[i], square[i - 1]])
		if suppose > 0:
			suppose = 1
		elif suppose < 0:
			suppose = -1
		s.append(suppose)
	# property lines/point analysis
	suppose = sum(s)
	if suppose == -4:
		return 2
	elif suppose == -3:
		return 1
	return 3


# point position relative to line
def for_edge(xy, edge):
	x, y = xy[0], xy[1]
	x1, y1 = edge[0][0], edge[0][1]
	x2, y2 = edge[1][0], edge[1][1]
	return (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)


# get path to files
square_path, points_path = sys.argv[1], sys.argv[2]
# list of coord`s of the vertices of a 'square'
with open(square_path, 'r') as square_file:
	# sq_coord == [[x1, y1], ... , [x4, y4]]
	sq_coord = [[float(j) for j in i.split(' ')] for i in square_file]
# list of coord`s of the points
with open(points_path, 'r') as points_file:
	# pp_coord == [[x1, y1], [x2, y2], ... , [x4, y4]]
	pp_coord = [[float(j) for j in i.split(' ')] for i in points_file]

for i in pp_coord:
	print(pp_property(i, sq_coord))
