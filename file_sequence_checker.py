# Feb 12, 2017
# Get a list of filenames. Extract the numerical sequence, and make sure all
# the entries are there.

# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjWzu7Vk4vSAhWHrVQKHeKzAKgQFggcMAA&url=http%3A%2F%2Fstackoverflow.com%2Fquestions%2F3964681%2Ffind-all-files-in-directory-with-extension-txt-in-python&usg=AFQjCNFscnTWu4OERT0WfRkhiNO0WL_zGg&sig2=xKqfQDPS3xj3ozgn5-Prlg

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

