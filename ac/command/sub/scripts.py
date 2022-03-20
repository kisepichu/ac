# coding: utf-8

from datetime import datetime, timedelta
from command.sub.colors import *
from command.sub.format_statement import pat

def print_dltestcases(testcase_num):
	if testcase_num == -1:
		print(f'skipped')
	else:
		print(f'downloaded {testcase_num} testcases')

def print_status(status, testcase_num=1, end='\n'):
	if status == 'AC' or status == 'OK':
		print(CACBG + status + CEND, end='')
	elif status in ['TLE','WA','RE']:
		print(CWABG + status + CEND, end='')
	elif status == 'CE':
		print(CCEBG + status + CEND, end='')
	else:
		print(CCEBG + status + CEND, end='')
	if not testcase_num:
		print(' ' + CWABG + 'NT' + CEND, end='')
	print(end, end='')

def query_submit():
	print('submit? [Y,n]: ', end="")
	return(input() in ['Y','y'])

def print_submitted(f):
	if f:
		print(CAC + 'submitted' + CEND)
	else:
		print(CCE + 'not submitted' + CEND)

def print_case(num, input, expected, output, result, istest=1):
	if istest:
		print(f' ===== case {num} ===== ')
	print('input:\n' + input)
	if istest:
		print('expected:\n' + expected)
	print('output:\n' + output)
	print_status(result)

def print_summary(cnt, results):
	tle_exists = 0
	for r in results:
		if r == 'TLE':
			tle_exists = 1
	print('┏' + '━' * (12+tle_exists) + '┓')
	for i in range(cnt):
		print(f'┃ case {i+1}: ', end='')
		print_status(results[i], end='')
		if tle_exists and results[i] != 'TLE':
			print(' ', end='')
		print(' ┃')
	print('┗' + '━' * (12+tle_exists) + '┛')

def print_statement(statement):
	for before, after in pat:
		statement=statement.replace(before, after)
	print(statement)

def print_time():
	print(CGRAY + str(datetime.now()) + CEND)
