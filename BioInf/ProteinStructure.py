#!/usr/bin/env python

from Bio.PDB import PDBParser,PDBList

import os

PDB_REPO = os.path.dirname(__file__) + "/pdb_repo/"
pdbList = PDBList()
pdbParser = PDBParser()

class BadProteinCode(Exception):
	def __init__(self,proteinName):
		self.name = proteinName
	def __str__(self):
		return repr("Protein code {} doesn't exist or there's a network error".format(self.name))

class PSData(object):
	'''Class to contain all data relevant to a protein structure and graph representation'''
	def __init__(self,protein_code, dir_addon=""):
		try:
			self._structure = pdbParser.get_structure(protein_code,\
				pdbList.retrieve_pdb_file(protein_code,pdir=PDB_REPO+dir_addon))
		except IOError:
			raise BadProteinCode(protein_code)
		self._pdb_code = protein_code

		self._metrics_list = dict()

	def pdb_code():
	    # doc = "The pdb_code property. pdb_code is read-only!"
	    def fget(self):
	        return self._pdb_code
	    def fset(self, value):
	         raise AttributeError("pdb_code is read-only\n The object's pdb code is %s"%self._pdb_code)
	    # def fdel(self):
	    #     del self._pdb_code
	    return locals()
	pdb_code = property(**pdb_code())

	def __getitem__(self,metric_name):
		return self._metrics_list[metric_name]['metric_data']	

	def __setitem__(self,metric_name,new_metric):
		self._metrics_list[metric_name] = new_metric

	@property
	def available_metrics(self):
		return self._metrics_list.keys()

	@property
	def structure(self):
		return self._structure



if __name__ == '__main__':
	tst_pdb = PSData('1mbn')
	tst_pdb.pdb_code = '4nbn'