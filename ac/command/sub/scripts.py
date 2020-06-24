# coding: utf-8

from command.sub.colors import *

def print_dltestcases(testcase_num):
	if testcase_num == -1:
		print(f'skipped')
	else:
		print(f'downloaded {testcase_num} testcases')

def print_status(status, testcase_num):
	print(CCEBG+'TEST'+CEND)
	if status == 'AC':
		print(CACBG + 'AC' + CEND, end='')
	elif status == 'WA':
		print(CWABG + 'WA' + CEND, end='')
	elif status == 'CE':
		print(CCEBG + 'CE' + CEND, end='')
	else:
		print(CCEBG + status + CEND, end='')
	if not testcase_num:
		print(CWABG + 'NT' + CEND, end='')
	print()

def query_submit():
	print('submit? [Y,n]', end="")
	return(input() in ['Y','y'])
