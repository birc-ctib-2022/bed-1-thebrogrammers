"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from tracemalloc import start
from unicodedata import name
from bed import (
	BedLine, parse_line, print_line
)
from query import Table


def main() -> None:
	"""Run the program."""
	# Setting up the option parsing using the argparse module
	argparser = argparse.ArgumentParser(
		description="Extract regions from a BED file")
	argparser.add_argument('bed', type=argparse.FileType('r'))
	argparser.add_argument('query', type=argparse.FileType('r'))

	# 'outfile' is either provided as a file name or we use stdout
	argparser.add_argument('-o', '--outfile',  # use an option to specify this
						   metavar='output',  # name used in help text
						   type=argparse.FileType('w'),  # file for writing
						   default=sys.stdout)

	# Parse options and put them in the table args
	args = argparser.parse_args()

	# With all the options handled, we just need to do the real work
	# FIXME: put your code here

	table = Table()

	for line in args.bed:
		table.add_line(parse_line(line))

	for line in args.query:
		chrom, startstring, stopstring = line.split()
		start = int(startstring)
		stop = int(stopstring)
		
		for each in table.get_chrom(chrom):
			if each.chrom_start >= start and each.chrom_end<=stop:
				print_line(BedLine(chrom,each.chrom_start,each.chrom_end,each.name),args.outfile)




if __name__ == '__main__':
	main()
