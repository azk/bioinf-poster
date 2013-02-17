#!/usr/bin/env python

from Bio.PDB import PDBList,PDBParser

from scipy.spatial.distance import euclidean

import networkx as nx
import matplotlib.pyplot as plt

from pprint import pprint as pp
from numpy import zeros


distanceThreshold = 1 #sys.argv[2]

pdbl = PDBList()
pdbp = PDBParser()

pro_name = '1MBN'
structure =  pdbp.get_structure(pro_name,pdbl.retrieve_pdb_file(pro_name))
atom_cords = {at.get_serial_number():{"cord" : at.get_coord()} for at in structure.get_atoms()}

mtrxSize = max(atom_cords.keys())
distanceMatrix = zeros([mtrxSize,mtrxSize])

atom_graph = nx.Graph()

def genDistances(atm):
	cord = atom_cords[atm]["cord"]
	for atm2,cord2 in atom_cords.iteritems():
		if atm2 >= atm:
			continue
		distanceMatrix[atm-1,atm2-1] = euclidean(cord,cord2["cord"])
# for atm in atom_cords.keys():
# 	genDistances(atm)

# pp(distanceMatrix)
