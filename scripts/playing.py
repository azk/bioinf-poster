#!/usr/bin/env python

from Bio.PDB import PDBList,PDBParser,Selection

import networkx as nx
import matplotlib.pyplot as plt

from pprint import pprint as pp

import numpy as np

distanceThreshold = 1 #sys.argv[2]

pdbList = PDBList()
pdbParser = PDBParser()

proteinName = '1MBN'
structure =  pdbParser.get_structure(proteinName,pdbList.retrieve_pdb_file(proteinName))

resList = Selection.unfold_entities(structure,'R')
distanceMatrix = np.zeros([len(resList),len(resList)])

def genDistanceMatrix(dMatrix,rList):	
	caMap = {res.id[1] : res['CA'] for res in rList if 'CA' in res}
	
	pp(caMap)
	pp(len(caMap))

genDistanceMatrix(distanceMatrix,resList)
# for atm in atom_cords.keys():
# 	genDistances(atm)

# pp(distanceMatrix)
