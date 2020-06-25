# coding: utf-8

from command.sub.colors import *

def print_dltestcases(testcase_num):
	if testcase_num == -1:
		print(f'skipped')
	else:
		print(f'downloaded {testcase_num} testcases')

def print_status(status, testcase_num=1):
	if status == 'AC':
		print(CACBG + status + CEND, end='')
	elif status in ['TLE','WA','RE']:
		print(CWABG + status + CEND, end='')
	elif status == 'CE':
		print(CCEBG + status + CEND, end='')
	else:
		print(CCEBG + status + CEND, end='')
	if not testcase_num:
		print(' ' + CWABG + 'NT' + CEND, end='')
	print()

def query_submit():
	print('submit? [Y,n]: ', end="")
	return(input() in ['Y','y'])

def print_submitted(f):
	if f:
		print(CAC + 'submitted' + CEND)
	else:
		print(CCE + 'not submitted' + CEND)

def print_case(input, expected, output, result):
	print('print_case')

def print_summary(cnt, results):
	for i in range(cnt):
		print(f'case {i+1}: ', end='')
		print_status(results[i])