from Bio.PDB import PDBParser,PDBList,Selection


class PSData(object):
	'''Class to contain all data relevant to a protein structure and graph representation'''
	def __init__(proteinCode):
		self.structure = pdbParser.get_structure(proteinName,\
			pdbList.retrieve_pdb_file(proteinName))