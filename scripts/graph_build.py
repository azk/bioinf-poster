#!/usr/bin/env python

import networkx as nx

def build_graph_from_distance_matrix(dist_matrix,threshold):
	graph = nx.Graph()

	for i in range(dist_matrix.shape[0]):
		for j in range(dist_matrix.shape[1]):
			if i >= j:
				if dist_matrix[i,j] <= threshold and dist_matrix[i,j] != 0:
					graph.add_edge(i,j)#,weight = dist_matrix[i,j])

	return graph


def write_simple_file(graph,file_name):
	with open('./graph.txt','w') as f:
		for e in graph.edges():
			f.write("{} {}\n".format(e[0],e[1]))