import csv
import os
from collections import Counter
from pprint import pprint as pp
from string import join

from itertools import combinations
import networkx as nx
out_dir = "graphs/motif_graph"

from graph_build import write_simple_file

motif_graph = nx.Graph()

for path,dirs,files in os.walk('graphs/ec_hs_culled_30each_smallest'):
	files = filter(lambda x: "MAT" in x and "_5_" not in x and "_3_" not in x,files)
	for f in files:
		motifs_in_protein = []
		with open(os.path.join(path,f),'r') as csvf:
			reader = csv.reader(csvf,delimiter=' ')
			for row in reader:
				zscore = float(row[4])
				uniq = float(row[6])
				mfact = float(row[7])
				if  zscore > 2.0 and zscore != 888888 and uniq >= 4 and mfact > 1.1:
				# if  uniq >= 4 and mfact > 1.10:
					motifs_in_protein.append(row[0])
		for x,y in combinations(motifs_in_protein,2):
			motif_graph.add_edge(x,y)

write_simple_file(motif_graph,out_dir+".txt")			

