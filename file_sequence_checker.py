# Feb 12, 2017
# Get a list of filenames. Extract the numerical sequence, and make sure all
# the entries are there.

# Refs:
# 	Glob: http://stackoverflow.com/a/3964691
# 	Regex: http://stackoverflow.com/a/4289348

import os
import glob
import re

# Set working directory
path = "/Users/Emma/Desktop/youtube-dl/"
os.chdir(path)

sequence = []

# Grab first number from each filenames in working dir
# (And don't whinge if it finds files without numbers)
for filename in glob.glob("*"):
	digits = re.findall(r'\d+', filename)

	for each in digits:
		try:
			sequence.append(int(each[0]))
		except:
			pass

# Generate a complete sequence to compare against
gen_seq = [s for s in range(1,318)]

# Print us some nice output
print(sequence)
print(gen_seq)

if sequence == gen_seq:
	print("Sequences are the same.")
else:
	print("SEQUENCES NOT SAME.") 

