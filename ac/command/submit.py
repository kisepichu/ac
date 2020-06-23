# coding: utf-8

import requests
import os
import lxml.html
import pathlib
import sys
from command.sub.format import format
from command.oj.atcoder import AtCoder
from command.oj.codeforces import CodeForces

def submit(args, config):
	# print(args)
	
	problem_number = ord(args.problem_char) - ord('a')

	with open('data/contest/problems.csv', encoding="utf-8_sig", mode='r') as f:
		problem = f.readlines()[problem_number].split(',')

	oj_name = problem[0]
	contest_id = problem[1]
	problem_id = problem[2]

	if oj_name == "atcoder":
		oj = AtCoder()
	elif oj_name == "codeforces":
		oj = CodeForces()
	else:
		raise Exception("no such online judge")
	
	oj.dev(problem)
	# format
	# oj.test()
	# oj.submit()

	return
