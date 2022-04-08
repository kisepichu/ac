# coding: utf-8

import os
import subprocess
import pyperclip
from command.sub.scripts import *
from command.sub.format import format
from command.sub.complement_problem_char import *
from command.oj.atcoder import AtCoder
from command.oj.codeforces import CodeForces
from command.oj.atcoderproblems import AtCoderProblems


def run(args, config):
    if args.testcase_num == 0:
        case_num = 0
        input = pyperclip.paste().encode()
        expected = "#not_test".encode()
        timelimit = 3
    elif args.testcase_num == -1:
        case_num = 0
        input = None
        expected = "#not_test".encode()
        timelimit = 99824
    elif args.testcase_num < -1:
        case_num = 0
        if "run_input" not in config:
            return
        input = config["run_input"]
        expected = "#not_test".encode()
        timelimit = 99824
    else:
        case_num = args.testcase_num
        timelimit = 3

        contest_id, problem_number = complement_problem_char(args, config)

        if contest_id == "":
            with open("data/contest/problems.csv", encoding="utf-8_sig", mode="r") as f:
                problem = f.readlines()[problem_number].split(",")
                problem[2] = problem[2][:-1]
                if problem[0] == "atcoder":
                    1  # oj = AtCoder()
                elif problem[0] == "codeforces":
                    1  # oj = CodeForces()
                else:
                    raise Exception(f"no such online judge: {problem[0]}")
        else:
            oj = AtCoder()
            problem = oj.get_problems(contest_id)[problem_number]

        test_dir = f"data/testcase/atcoder/{problem[1]}/"

        path = test_dir + f"{problem[2]}_{args.testcase_num}.input"
        if os.path.exists(path):
            with open(path, encoding="utf-8_sig", mode="r") as f:
                input = f.read().encode()
        else:
            raise Exception("testcase not found")

        if args.add_input:
            if "run_input" not in config:
                return
            input = (input.decode() + config["run_input"]).encode()

        path = test_dir + f"{problem[2]}_{args.testcase_num}.output"
        if os.path.exists(path):
            expected = None
            with open(path, encoding="utf-8_sig", mode="r") as f:
                expected = f.read().encode()

    result = "OK"
    try:
        output = subprocess.run(
            config["execute"].split(),
            input=input,
            stdout=subprocess.PIPE,
            check=1,
            timeout=timelimit,
        ).stdout.decode()
    except subprocess.CalledProcessError as e:
        result = "RE"
        output = "(RE)"
    except subprocess.TimeoutExpired as e:
        result = "TLE"
        output = "(TLE)"
    if expected.decode() != "#not_test" and output != expected.decode():
        result = "WA"

    if input is None:
        input = "(above)".encode()
    if "run_no_print_case" not in config:
        print_case(
            case_num,
            input.decode(),
            expected.decode(),
            output,
            result,
            args.testcase_num > 0,
        )
    return output
