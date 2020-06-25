# coding: utf-8

import sched
import time
from urllib.parse import urlparse
from command.oj.atcoder import AtCoder
from command.oj.codeforces import CodeForces
from command.oj.atcoderproblems import AtCoderProblems
from command.sub.scripts import *

def start(args, config, oj, contest_id):
	if args.show_a:
		print_statement(oj.get_statement_a(contest_id))
	url = urlparse(args.contest_url)
	problems = oj.get_problems(contest_id)
	for problem in problems:
		oj.download_testcases(problem)
	return

def init(args, config):
	url = urlparse(args.contest_url)
	if url.netloc == 'atcoder.jp':
		oj = AtCoder()
	elif url.netloc == 'codeforces.com':
		oj = CodeForces()
	elif url.netloc == 'kenkoooo.com':
		oj = AtCoderProblems()
	else:
		raise Exception('no such online judge: ' + url.netloc)

	contest_id = oj.get_contest_id(url.path[1:].split('/'))
	if contest_id is None:
		raise Exception('not a contest url: ', args.contest_url)

	start_time = oj.get_start_time(contest_id)
	
	sc = sched.scheduler(time.time, time.sleep)
	for i in range(1,31):
		u_time = int(time.mktime((start_time - timedelta(seconds=i)).timetuple()))
		sc.enterabs(u_time, 1, print_time)
	u_time = int(time.mktime(start_time.timetuple()))
	sc.enterabs(u_time, 1, start, (args, config, oj, contest_id, ))
	sc.run()

	# problems = oj.get_problems(url)
	
	# write to problems.csv

	return
