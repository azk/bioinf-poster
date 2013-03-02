#!/usr/bin/env python

from BioInf.ProteinStructure import PSData

EC_HS_DIR = "data/ec_classification/homo_sapiens/"

file_format = "ecNUM_hs.txt"

num_ecs = 6

for i in range(3,num_ecs+1):
	curr_file = EC_HS_DIR + file_format.replace("NUM",str(i))
	with open(curr_file,'r') as f:
		for line in f:
			splits = line.split()
			if splits == [] or splits[0] == "PDBID":
				continue
			else:
				try:
					PSData(splits[0],"ec_"+str(i)+"_hs")
				except:
					continue


