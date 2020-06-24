# coding: utf-8

import sys
import os
import argparse
import yaml

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from command.init import *
from command.submit import *
from command.copy import *
from command.clear import *
from command.make_snippet import *

def main():
	with open('config.yml', encoding="utf-8_sig", mode='r') as f:
		config = yaml.load(f, Loader=yaml.SafeLoader)

	parser = argparse.ArgumentParser(description='perf +100')
	subparsers = parser.add_subparsers()

	# init
	parser_init = subparsers.add_parser('init')
	parser_init.set_defaults(handler=init)

	# submit
	parser_submit = subparsers.add_parser('submit', help='see `submit -h`')
	parser_submit.add_argument('-c', '--choose', action='store_true', help='choose whether to submit')
	parser_submit.add_argument('-m', '--manual', action='store_true', help='')
	parser_submit.add_argument('problem_char', help='a-z')
	parser_submit.set_defaults(handler=submit)

	# copy
	parser_copy = subparsers.add_parser('copy')
	parser_copy.set_defaults(handler=copy)

	# clear
	parser_clear = subparsers.add_parser('clear')
	parser_clear.set_defaults(handler=clear)

	# make-snippet
	parser_make_snippet = subparsers.add_parser('make-snippet')
	parser_make_snippet.set_defaults(handler=make_snippet)
	
	args = parser.parse_args()
	if hasattr(args, 'handler'):
		args.handler(args,config)
	else:
		parser.print_help()

if __name__ == '__main__':
	main()
