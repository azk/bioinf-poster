#!/usr/bin/env python

import numpy as np
from Bio.PDB import Selection


class EuclidianMetric(object):

	def __call__(self,structure):
		res_list = Selection.unfold_entities(structure,'R')
		res_list = filter(lambda res: res.id[0] == " ",res_list)
		distance_matrix = np.zeros([len(res_list),len(res_list)])
		for i,res1 in enumerate(res_list):
			for j,res2 in enumerate(res_list):
				distance_matrix[i,j] = res1['CA'] - res2['CA']

		return distance_matrix

MetricsFactory = {
	"euclidian" : EuclidianMetric
}

