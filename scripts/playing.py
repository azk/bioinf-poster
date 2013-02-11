#!/usr/bin/env python

from Bio.PDB import PDBList,PDBParser

from scipy.spatial.distance import euclidean

import networkx as nx

from pprint import pprint as pp


distanceThreshold = 1 #sys.argv[2]

pdbl = PDBList()
pdbp = PDBParser()

pro_name = '1MBN'
structure =  pdbp.get_structure(pro_name,pdbl.retrieve_pdb_file(pro_name))
atom_cords = {at.get_serial_number():{"cord" : at.get_coord()} for at in structure.get_atoms()}
pp(atom_cords)
atom_graph = nx.Graph()
atom_graph.add_nodes_from(atom_cords.keys())






