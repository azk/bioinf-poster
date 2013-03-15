import subprocess
import os

"""mfinder <input network file name> [-s <motif size>]
			[-r <num of random networks>] [-f <output file name>]
														[more flags]"""

mfind_args = {
	"cmd" : "mfinder1.2\mfinder1.2.exe",
	"motif_size" : "6",
	"options" : "-nd -omat"
}

in_dir = "graphs\ec_hs_culled_30each_smallest"
from string import join

for dir_path, dirs, files in os.walk(in_dir):
	files = filter(lambda x: "MAT" not in x and "OUT" not in x,files)
	for f in files:
		cmd = join([mfind_args['cmd'],os.path.join(dir_path,f),"-s",mfind_args['motif_size'],mfind_args['options'],"-f",\
			os.path.join(dir_path,f+"_"+mfind_args['motif_size'])])
		# print cmd
		mfind = subprocess.Popen(cmd)
		mfind.wait()