#!/usr/bin/env python

from graph_build import *
from BioInf.MetricsFactory import MetricsFactory

from Bio.PDB import PDBParser

import os

SRC_DIR = "data/ec_hs_culled_30_smallest"
DST_DIR = "data/graphs/ec_hs_culled_30each_smallest"

euclidian = MetricsFactory['euclidian']()
parser = PDBParser()

for dir_path, dirs, files in os.walk(SRC_DIR):
	if files == []:
		continue
	destination = os.path.join(DST_DIR,\
		os.path.basename(dir_path))	
	if  not os.path.exists(destination):
		os.makedirs(destination)
	for f in files:
		strct = parser.get_structure("bla",os.path.join(dir_path,f))
		mtrx = euclidian(strct)
		grph = build_graph_from_distance_matrix(mtrx, 6)
		write_mfinder_file(grph,os.path.join(destination,f+"_graph.txt"))