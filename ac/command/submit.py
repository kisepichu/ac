# coding: utf-8

import requests
import os
import lxml.html
import pathlib
import sys
import subprocess
import yaml

from command.sub.format import format
from command.sub.test import test
from command.sub.scripts import *
from command.sub.complement_problem_char import *
from command.generate import generate
from command.oj.atcoder import AtCoder
from command.oj.codeforces import CodeForces


def submit(args, config):
    # print('args: ', args)
    # print('config: ', config)

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

    if args.source_path == "":
        source_path = config["source_path"]
    else:
        source_path = args.source_path

    # format
    with open(source_path, encoding="utf-8_sig", mode="r") as f:
        source = f.read()
    if not args.no_format:
        with open(config["formatted_path"], mode="w") as f:
            source = format(source)
            f.write(source)
        source_path = config["formatted_path"]

    # -f option
    if args.force:
        oj.submit(problem, config["language_id"], source)
        print_submitted(1)
        return

    # download testcases
    print_dltestcases(oj.download_testcases(problem))

    # compile
    if os.path.exists(config["executable_path"]):
        os.remove(config["executable_path"])
    if args.compile != "":
        subprocess.run(args.compile.replace("{{source}}", source_path).split())
    else:
        subprocess.run(config["compile"].replace("{{source}}", source_path).split())

    # test
    status, testcase_num, output_empty = test(config, problem)
    print_status(status, testcase_num)
    if status == "CE":
        return

    # submit
    submit_flag = 1
    if status != "AC":
        submit_flag = 0
    if args.choose or not testcase_num or output_empty:
        submit_flag = query_submit()
    if submit_flag:
        # print(problem, config['language_id'], source)
        oj.submit(problem, config["language_id"], source)
    print_submitted(submit_flag)

    # generate input for next problem

    problem_number += 1
    if problem_number >= 26:
        problem_number -= 26
        args.problem_char = chr(ord("a") + problem_number // 26) + chr(
            ord("a") + problem_number % 26
        )
    else:
        args.problem_char = chr(ord("a") + problem_number)
    if status == "AC":
        generate(args, config)
    return
