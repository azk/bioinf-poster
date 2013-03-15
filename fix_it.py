
import os

SRC_DIR = "data/graphs/ec_hs_culled_30each"
DST_DIR = "data/graphs/ec_hs_culled_30each_fixed"

for dir_path, dirs, files in os.walk(SRC_DIR):
	if files == []:
		continue
	destination = os.path.join(DST_DIR,\
		os.path.basename(dir_path))	
	if  not os.path.exists(destination):
		os.makedirs(destination)	
	for f in files:
		with open(os.path.join(dir_path,f),'r') as bad_f:
			with open(os.path.join(destination,f),'w') as out_f:
				for line in bad_f:
					splits = line.split()
					out_f.write("{} {} 1\n".format(splits[0],splits[1]))