# coding: utf-8

from urllib.parse import urlparse
from command.oj.atcoder import AtCoder
from command.oj.codeforces import CodeForces
from command.oj.atcoderproblems import AtCoderProblems

def init(args, config):
	url = urlparse(args.contest_url)
	if url['netloc'] == 'atcoder.jp':
		oj = AtCoder()
	elif url['netloc'] == 'codeforces.com':
		oj = CodeForces()
	elif url['netloc'] == 'kenkoooo.com':
		oj = AtCoderProblems()
	else:
		raise Exception(f'no such online judge: {url[\'netloc\']}')

	# wait until start time
	
	problems = oj.get_problems()
	
	# write to problems.csv

	return
