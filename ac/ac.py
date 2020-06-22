# coding: utf-8

import sys
import os
import argparse
from command.submit import *
from command.copy import *
from command.clear import *

def main():
	devnull = open(os.devnull, 'w')

	parser = argparse.ArgumentParser(description='perf +100')
	subparsers = parser.add_subparsers()

	# submit
	parser_submit = subparsers.add_parser('submit', help='see `submit -h`')
	parser_submit.add_argument('-c', '--choose', action='store_true', help='choose whether to submit')
	parser_submit.add_argument('problem_number', help='a-z')
	parser_submit.set_defaults(handler = submit)

	# copy
	parser_submit = subparsers.add_parser('copy')
	parser_submit.set_defaults(handler = copy)

	# clear
	parser_submit = subparsers.add_parser('clear')
	parser_submit.set_defaults(handler = clear)
	
	args = parser.parse_args()
	if hasattr(args, 'handler'):
		args.handler(args)
	else:
		parser.print_help()

if __name__ == '__main__':
	main()