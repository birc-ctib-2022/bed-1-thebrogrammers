# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_
import os
import filecmp
from query_bed import main

input_bed 	= "data/large.bed"
input_query1 = "data/query-1.txt"
output_bed1	= "data/testoutput1.bed"
expected1= "data/expected-1.txt"

input_query2 = "data/query-2.txt"
output_bed2	= "data/testoutput2.bed"
expected2= "data/expected-2.txt"

input_query3 = "data/query-3.txt"
output_bed3	= "data/testoutput3.bed"
expected3= "data/expected-3.txt"

def test_query_bed():

	os.system("python src/query_bed.py " + input_bed + " " + input_query1 + " -o" + output_bed1)
	os.system("python src/query_bed.py " + input_bed + " " + input_query2 + " -o" + output_bed2)
	os.system("python src/query_bed.py " + input_bed + " " + input_query3 + " -o" + output_bed3)
	assert filecmp.cmp(output_bed1, expected1)
	assert filecmp.cmp(output_bed2, expected2)
	assert filecmp.cmp(output_bed3, expected3)
