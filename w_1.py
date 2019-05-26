import numpy as np
import math
import copy
from collections import Counter

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

def squared_error_distortion(k, m, centers, data):
	s = 0
	for point in data:
		s += (distance_from_datapoint_to_centers(centers, point))**2
	n = len(data)
	return s/n


def form_clusters(centers_assigned, data, k):
	clusters_with_points = [[] for i in range(k)]
	for i in range(len(centers_assigned)):
		j = centers_assigned[i]
		clusters_with_points[j].append(data[i])

	return clusters_with_points

def average(l):
    llen = len(l)
    def divide(x): return x / llen
    return list(map(divide, map(sum, zip(*l))))

def new_centers(clusters_with_points, k):
	c = []
	for l in clusters_with_points:
		c.append(average(l))
	return c

def kmeans(k, m, data):
	centers = data[0:k]
	centers_assigned = [0 for i in range(len(data))]
	centers_ = []
	while True:

		#centers_ = copy.deepcopy(centers)
		for i in range(len(data)):
			point = data[i]
			val = float('Inf')
			for j in range(len(centers)):
				s = dist(point, centers[j])
				if s < val:
					val = s
					centers_assigned[i] = j
		clusters_with_points = form_clusters(centers_assigned, data, k)
		c = new_centers(clusters_with_points, k)
		if set(map(tuple,c)) == set(map(tuple,centers)):
			break
		else:
			centers = c
	return centers
		

k = 6
m = 5
data = farthest_first_traversal_input('kmeans.txt')
centers = kmeans(k, m, data)
for i in centers:
	for k in i:
		print("%.3f"%k, end = ' ')
	print('')








'''
k = 5
m = 2
centers = farthest_first_traversal_input('centers.txt')
data = farthest_first_traversal_input('data.txt')
print(squared_error_distortion(k, m, centers, data))
'''

'''
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
'''


