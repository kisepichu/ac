# coding: utf-8

import os
import pyperclip
from command.sub.scripts import *
from command.sub.complement_problem_char import *
from command.oj.atcoder import AtCoder
from command.oj.codeforces import CodeForces


def case(args, config):
    contest_id, problem_number = complement_problem_char(args, config)

    if contest_id == "":
        with open("data/contest/problems.csv", encoding="utf-8_sig", mode="r") as f:
            problem = f.readlines()[problem_number].split(",")
            problem[2] = problem[2][:-1]
            if problem[0] == "atcoder":
                oj = AtCoder()
            elif problem[0] == "codeforces":
                oj = CodeForces()
            else:
                raise Exception(f"no such online judge: {problem[0]}")
    else:
        oj = AtCoder()
        problem = oj.get_problems(contest_id)[problem_number]

    if args.command == "copy":
        test_dir = f"data/testcase/atcoder/{problem[1]}/"
        path = test_dir + f"{problem[2]}_{args.testcase_num}.input"
        if not os.path.exists(path):
            raise Exception("not exists")
        with open(path, encoding="utf-8_sig", mode="r") as f:
            pyperclip.copy(f.read())

        return
    elif args.command == "add":
        1
    elif args.command == "remove":
        1
    else:
        1

    return
