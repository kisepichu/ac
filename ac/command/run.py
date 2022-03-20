# coding: utf-8

import os
import subprocess
import pyperclip
from command.sub.scripts import *
from command.sub.format import format


def run(args,config):
	input = pyperclip.paste()
	result = 'OK'
	try:
		output = subprocess.run(config['execute'].split(), input=input.encode(), stdout=subprocess.PIPE, check=1, timeout=3).stdout.decode()
	except subprocess.CalledProcessError as e:
		result = 'RE'
		output = '(RE)'
	except subprocess.TimeoutExpired as e:
		result = 'TLE'
		output = '(TLE)'

	print_case(0, input, '', output, result, 0)
	return
