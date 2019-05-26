import numpy as np
import math

def farthest_first_traversal_input(file):
	read = open(file)
	data = []
	for line in read:
		vector = line.split(' ')
		vector = list(map(float, vector))
		data.append(vector)

	return data

def dist(x, y):
	d = 0
	for i in range(len(x)):
		d += (x[i] - y[i])**2
	return math.sqrt(d)

def distance_from_datapoint_to_centers(centers, datapoint):

	return min([dist(datapoint, center) for center in centers])

def max_distance(data, centers):
	max_point = None
	max_dist = float('-Inf')
	for point in data:
		if point not in centers:
			d = distance_from_datapoint_to_centers(centers, point) 
			if d > max_dist:
				max_dist = d
				max_point = point

	return max_point


def farthest_first_traversal(data, k, m):
	#i = [np.random.choice(data.shape[0], 1, replace = False)]
	centers = [data[0]]
	#return centers
	while len(centers) < k:
		max_point = max_distance(data, centers)
		#print(max_point)
		centers.append(max_point)
	return centers


file = 'farthest.txt'
k = 4
m = 4
data = farthest_first_traversal_input(file)
c = farthest_first_traversal(data, k, m)
#print(c)
for i in c:
	for k in i:
		print(k, end = ' ')
	print('')


