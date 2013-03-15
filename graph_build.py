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


def write_simple_file(graph,file_path):
	write_simple_graph(graph, file_path)

def write_sif_file(graph,file_path):
	write_simple_graph(graph, file_path, edge_interaction="pp")

def write_mfinder_file(graph,file_path):
	write_simple_graph(graph, file_path, edge_weight="1")

def write_simple_graph(graph, file_path,edge_interaction="",edge_weight=""):
	with open(file_path,'w') as f:
		for e in graph.edges():
			f.write("{}".format(e[0]))
			if edge_interaction != "":
				f.write(" {}".format(edge_interaction))
			f.write(" {}".format(e[1]))
			if edge_weight != "":
				f.write(" {}".format(edge_weight))
			f.write("\n")
