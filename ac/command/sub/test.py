# coding: utf-8

import os
import subprocess
from command.sub.scripts import *
from command.sub.format_ans import format_ans

def test(config, problem):
	test_dir = f'data/testcase/atcoder/{problem[1]}/'
	if not os.path.exists(config['executable_path']):
		return 'CE', -1

	results = []
	results_or = 0
	cnt = 0
	while os.path.exists(test_dir + f'{problem[2]}_{cnt+1}.input'):
		cnt += 1

		result = 'WJ'
		with open(test_dir + f'{problem[2]}_{cnt}.input', encoding='utf-8_sig', mode='r') as f:
			input = f.read()
		try:
			output = subprocess.run(config['execute'].split(), input=input.encode(), stdout=subprocess.PIPE, timeout=3)
		except subprocess.CalledProcessError as e:
			result = 'RE'
			results_or |= 4
		except subprocess.TimeoutExpired as e:
			result = 'TLE'
			results_or |= 1
		# proc = subprocess.Popen(config['execute'].split(), stdout=subprocess.PIPE)
		# output = proc.communicate(input)[0]
		# exit_code = proc.returncode

		with open(test_dir + f'{problem[2]}_{cnt}.output', encoding='utf-8_sig', mode='r') as f:
			expected = f.read()

		if result == 'WJ':
			if format_ans(output) == format_ans(expected):
				result = 'AC'
			else:
				result = 'WA'
				results_or |= 2

		print_case(input, expected, output, result)
		results.append(result)

	result = 'WJ'
	if results_or >= 4:
		result = 'RE'
	elif results_or >= 2:
		result = 'WA'
	elif results_or >= 1:
		result = 'TLE'
	else:
		result = 'AC'

	print_summary(cnt, results)

	return result, cnt
