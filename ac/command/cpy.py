# coding: utf-8

import os
import pyperclip
from command.sub.format import format


def cpy(args,config):
	if args.source_path == '':
		source_path = config['source_path']
	else:
		source_path = args.source_path

	# format
	with open(source_path, encoding="utf-8_sig", mode='r') as f:
		source = f.read()
	if not args.no_format:
		with open(config['formatted_path'], mode='w') as f:
			source = format(source)
			f.write(source)
		source_path = config['formatted_path']
	pyperclip.copy(source)
	return