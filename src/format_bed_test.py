import os
import filecmp
# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_
from format_bed import main

input 	= "data/input.bed"
output	= "data/testoutput.bed"
expected= "data/output.bed"

def test_format_bed():

	os.system("python src/format_bed.py " + input + " " + output)
	assert filecmp.cmp(output, expected)
