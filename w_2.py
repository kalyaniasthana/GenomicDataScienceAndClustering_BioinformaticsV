import math
import numpy as np
import copy


def distance_matrix_input(file):
	read = open(file)
	mat = []
	for line in read:
		l = line.strip()
		l = l.split(' ')
		l = list(map(float, l))
		mat.append(l)
	return mat


def hierarchical_clustering(mat, n):
	global distances
	distances = np.array(mat)
	new_node = copy.deepcopy(n)
	clusters = {}
	for i in range(0, n):
		clusters[i] = [i]
	new_distances = copy.deepcopy(distances)
	while len(clusters) > 1:
		def distance_between_clusters(i, j):
			if i in clusters and j in clusters:
				d = sum([distances[x, y] for x in clusters[i] for y in clusters[j]])/(len(clusters[i])*len(clusters[j]))
				return d
			return 0
		def find_closest_clusters():
			min_element = np.min(new_distances[np.nonzero(new_distances)])
			index = np.where(new_distances == min_element)[0]
			i = index[0]
			j = index[1]
			return (i, j)

		i, j = find_closest_clusters()

		p = [x+1 for x in clusters[i]]
		q = [x+1 for x in clusters[j]]
		for x in p:
			print(x, end = ' ')
		for x in q:
			print(x, end = ' ')
		print('')
		clusters[new_node] = clusters[i] + clusters[j]
	
		del clusters[i]
		del clusters[j]

		new_row = [distance_between_clusters(i, new_node) for i in range(len(distances))] 
		distances = np.concatenate((distances, [new_row]))
		new_distances = np.concatenate((new_distances, [new_row]))

		m = []
		for dist in new_row:
			m.append([dist])
		m.append([float(0)])
		distances = np.append(distances, m, axis = 1)
		new_distances = np.append(new_distances, m, axis = 1)
		new_distances[i] = [0 for i in range(len(new_distances))]
		new_distances[j] = [0 for i in range(len(new_distances))]
		new_distances[:, i] = [0 for i in range(len(new_distances))]
		new_distances[:, j] = [0 for i in range(len(new_distances))]
		new_node += 1


	return None


n = 20
file = 'hierarchical.txt'
mat = distance_matrix_input(file)
print(hierarchical_clustering(mat, n))