import csv
import os
from collections import Counter
from pprint import pprint as pp
from string import join
out_dir = "graphs"

ids = []
motif_counts = dict()
for path,dirs,files in os.walk('graphs/ec_hs_culled_30each_smallest'):
	files = filter(lambda x: "MAT" in x and "_5_" not in x and "_3_" not in x ,files)
	# if dirs == []:
	# 	out_file = open(os.path.join(out_dir,os.path.basename(path)+"_5_len_motif_summary.txt"),'w')
	for f in files:
		# out_file.write("%s:"%f[3:7])
		# print "\n====Motifs in file %s=======\n"%f
		with open(os.path.join(path,f),'r') as csvf:
			reader = csv.reader(csvf,delimiter=' ')
			for row in reader:
				zscore = float(row[4])
				uniq = float(row[6])
				mfact = float(row[7])
				if  zscore > 2.0 : # and mfact > 1.10:
					ids.append(row[0])
					if row[0] not in motif_counts.keys():
						motif_counts[row[0]] = Counter()
					motif_counts[row[0]][os.path.basename(path)] += 1
					# out_file.write(" " + row[0])
		# out_file.write("\n")
	# if dirs == []:
		# out_file.close()

					# print row
		# print "\n===================\n"

id_counts = Counter(ids)
pp(id_counts.most_common())
pp(motif_counts)
templ = "ec_?_hs"
with open("recurrences_4.txt",'w') as out_f:
	for motif in motif_counts.keys():
		out_f.write(motif)
		for i in range(1,7):
			ec_name = templ.replace("?",str(i))
			out_f.write(" "+ str(motif_counts[motif][ec_name]))
		out_f.write("\n")


