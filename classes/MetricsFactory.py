#!/usr/bin/env python

import numpy as np
from Bio.PDB import Selection

def euclidian_metric_imp(structure):
	res_list = Selection.unfold_entities(structure,'R')[0:152]	
	distance_matrix = np.zeros([len(res_list),len(res_list)])
	for i,res1 in enumerate(res_list):
		for j,res2 in enumerate(res_list):
			distance_matrix[i,j] = res1['CA'] - res2['CA']

	return distance_matrix

def default_euclidian_metric():
	return euclidian_metric_imp

MetricsFactory = {
	"euclidian" : default_euclidian_metric
}


