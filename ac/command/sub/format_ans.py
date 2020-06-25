# coding: utf-8

def format_ans(s):
	s = s.replace('\n',' ').replace('\r',' ')
	t = s.split()
	u = ''
	for line in t:
		if len(line):
			u += line + ' '

	return u
