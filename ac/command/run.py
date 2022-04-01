# coding: utf-8

import os
import subprocess
import pyperclip
from command.sub.scripts import *
from command.sub.format import format


def run(args, config):
    if args.testcase_num == 0:
        case_num = 0
        input = pyperclip.paste().encode()
        expected = "#not_test".encode()
        timelimit = 3
    elif args.testcase_num < 0:
        case_num = 0
        input = None
        expected = "#not_test".encode()
        timelimit = 99824
    else:
        case_num = args.testcase_num
        timelimit = 3
        if args.problem_char == "$":
            args.problem_char = config["contest_data"]["resent_problem_char"]
        else:
            with open("data/contest/contest_data.yml", "w") as f:
                config["contest_data"]["resent_problem_char"] = args.problem_char
                yaml.dump(config["contest_data"], f)

        if ord("a") <= ord(args.problem_char[0]) and ord(args.problem_char[0]) <= ord(
            "z"
        ):
            if len(args.problem_char) == 1:
                problem_number = ord(args.problem_char) - ord("a")
            else:
                problem_number = (ord(args.problem_char[0]) - ord("a") + 1) * 26 + (
                    ord(args.problem_char[1]) - ord("a")
                )

        with open("data/contest/problems.csv", encoding="utf-8_sig", mode="r") as f:
            problem = f.readlines()[problem_number].split(",")
            problem[2] = problem[2][:-1]

        test_dir = f"data/testcase/atcoder/{problem[1]}/"

        path = test_dir + f"{problem[2]}_{args.testcase_num}.input"
        if os.path.exists(path):
            with open(path, encoding="utf-8_sig", mode="r") as f:
                input = f.read().encode()
        else:
            print("testcase not found")
            return
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
    print_case(
        case_num,
        input.decode(),
        expected.decode(),
        output,
        result,
        args.testcase_num > 0,
    )
    return
