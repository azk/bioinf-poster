#!/usr/bin/env python

import shutil
import os
import re

from BioInf.ProteinStructure import PDB_REPO

CULLED_FILE = "data/culled_pdb"
culled_list = []

with open(CULLED_FILE,'r') as f:
	for line in f:
		splits = line.split()
		if len(splits) == 0 or splits[0] == "IDs":
			continue
		else:
			culled_list.append(splits[0].lower()[:-1])

pdb_file_pattern = re.compile("pdb(?P<prot_name>[0-9a-z]+).ent")
def not_in_culled(dir_name,file_list):
	# print os.path.basename(dir_name)
	if os.path.basename(dir_name) == "ec_hs":
		return []
	else:
		not_culled = []
		for pdb_file in file_list:
			
			pdb_name = pdb_file_pattern.match(pdb_file).group('prot_name')
			# print "%d: %s => %s"%(not_in_culled.processed,pdb_file,pdb_name)
			not_in_culled.processed+=1
			if pdb_name not in culled_list:
				not_culled.append(pdb_file)
		return not_culled
not_in_culled.processed = 1

shutil.copytree(PDB_REPO+"ec_hs",PDB_REPO+"culled_ec_hs",ignore=not_in_culled)

# print culled_list