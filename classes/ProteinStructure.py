#!/usr/bin/env python

from Bio.PDB import PDBParser,PDBList,Selection

pdbList = PDBList()
pdbParser = PDBParser()

class BadProteinCode(Exception):
	def __init__(self,proteinName):
		self.name = proteinName
	def __str__(self):
		return repr("Protein code {} doesn't exist or there's a network error".format(self.name))


class PSData(object):
	'''Class to contain all data relevant to a protein structure and graph representation'''
	def __init__(self,protein_code,first_metric='euclidian'):

		try:
			self._structure = pdbParser.get_structure(protein_code,\
				pdbList.retrieve_pdb_file(protein_code))
		except IOError:
			raise BadProteinCode(protein_code)
		self._pdb_code = protein_code
		self.add_metric(first_metric)


	def pdb_code():
	    doc = "The pdb_code property. pdb_code is read-only!"
	    def fget(self):
	        return self._pdb_code
	    def fset(self, value):
	         raise AttributeError("pdb_code is read-only\n The object's pdb code is %s"%self._pdb_code)
	    # def fdel(self):
	    #     del self._pdb_code
	    return locals()
	pdb_code = property(**pdb_code())

	def add_metric(self,new_metric):
		try:
			distance_func = DistanceMatrixFactory(new_metric)
			distance_func(self._structure)
		except:
			pass

		self._metrics_list['new_metric'] = (distance_func,new_matrix)



if __name__ == '__main__':
	tst_pdb = PSData('1mbn')
	tst_pdb.pdb_code = '4nbn'