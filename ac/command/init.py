# coding: utf-8

import sched
import time
from datetime import datetime
from urllib.parse import urlparse
from command.oj.atcoder import AtCoder
from command.oj.codeforces import CodeForces
from command.oj.atcoderproblems import AtCoderProblems
from command.sub.scripts import *


def start(args, config, oj, contest_id):
    if args.show_a:
        print_statement(oj.get_statement_a(contest_id, 1))

    url = urlparse(args.contest_url)
    problems = oj.get_problems(contest_id, 1)

    if args.download:
        for problem in problems:
            oj.download_testcases(problem)

    with open('data/contest/problems.csv', mode='w') as f:
        for problem in problems:
            f.write(','.join(problem)+'\n')

    return


def init(args, config):
<<<<<<< HEAD
	if not args.contest_url.startswith('http'):
		args.contest_url = 'https://atcoder.jp/contests/' + args.contest_url
	url = urlparse(args.contest_url)
	if url.netloc == 'atcoder.jp':
		oj = AtCoder()
	elif url.netloc == 'codeforces.com':
		oj = CodeForces()
	elif url.netloc == 'kenkoooo.com':
		oj = AtCoderProblems()
	else:
		raise Exception('no such online judge: ' + url.netloc)

	contest_id = oj.get_contest_id(url)
	if contest_id is None:
		raise Exception('not a contest url: ', args.contest_url)

	start_time = oj.get_start_time(contest_id)
	print(f'start time: {start_time}')
	
	sc = sched.scheduler(time.time, time.sleep)
	if start_time > datetime.now():
		for i in range(1,31):
			u_time = int(time.mktime((start_time - timedelta(seconds=i)).timetuple()))
			sc.enterabs(u_time, 1, print_time)
	u_time = int(time.mktime(start_time.timetuple()))
	sc.enterabs(u_time, 1, start, (args, config, oj, contest_id, ))
	sc.run()

	return
=======
    if not args.contest_url.startswith('http'):
        args.contest_url = 'https://atcoder.jp/contests/' + args.contest_url
    url = urlparse(args.contest_url)
    if url.netloc == 'atcoder.jp':
        oj = AtCoder()
    elif url.netloc == 'codeforces.com':
        oj = CodeForces()
    elif url.netloc == 'kenkoooo.com':
        oj = AtCoderProblems()
    else:
        raise Exception('no such online judge: ' + url.netloc)

    contest_id = oj.get_contest_id(url)
    if contest_id is None:
        raise Exception('not a contest url: ', args.contest_url)

    start_time = oj.get_start_time(contest_id)
    print(f'start time: {start_time}')

    sc = sched.scheduler(time.time, time.sleep)
    if start_time > datetime.now():
        for i in range(1, 31):
            u_time = int(time.mktime(
                (start_time - timedelta(seconds=i)).timetuple()))
            sc.enterabs(u_time, 1, print_time)
    u_time = int(time.mktime(start_time.timetuple()))
    sc.enterabs(u_time, 1, start, (args, config, oj, contest_id, ))
    sc.run()

    return
>>>>>>> dev
