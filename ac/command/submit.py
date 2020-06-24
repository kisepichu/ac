# coding: utf-8

import requests
import os
import lxml.html
import pathlib
import sys
import subprocess
from command.sub.format import format
from command.sub.test import test
from command.sub.scripts import *
from command.oj.atcoder import AtCoder
from command.oj.codeforces import CodeForces

def submit(args, config):
	# print('args: ', args)
	# print('config: ', config)

	devnull = open(os.devnull, 'w')
	
	problem_number = ord(args.problem_char) - ord('a')

	with open('data/contest/problems.csv', encoding="utf-8_sig", mode='r') as f:
		problem = f.readlines()[problem_number].split(',')
		problem[2]=problem[2][:-1]

	if problem[0] == 'atcoder':
		oj = AtCoder()
	elif problem[0] == 'codeforces':
		oj = CodeForces()
	else:
		raise Exception(f'no such online judge: {oj_name}')
	
	# format
	with open(config['source_path'], encoding="utf-8_sig", mode='r') as f:
		source = f.read()
	with open(config['formatted_path'], mode='w') as f:
		source = format(source)
		f.write(source)
	
	# download testcases
	print_dltestcases(oj.download_testcases(problem))

	# compile
	if os.path.exists(config['executable_path']):
		os.remove(config['executable_path'])
	subprocess.run(config['compile'].split())
	if not os.path.exists(config['executable_path']):
		print_status('CE', -1)
		return

	# test
	status, testcase_num = test(f'data/testcase/atcoder/{problem[1]}/')
	print_status(status, testcase_num)

	# submit
	submit_flag = 1
	if status == 'WA':
		submit_flag = 0
	if args.choose or not testcase_num:
		submit_flag = query_submit()
	if submit_flag:
		print(problem, config['language_id'], source)
		oj.submit(problem, config['language_id'], source)
	print_submitted(submit_flag)
	return
