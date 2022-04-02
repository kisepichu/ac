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
from command.sub.predict import *
from command.oj.atcoder import AtCoder
from command.oj.codeforces import CodeForces


def generate(args, config):
    # print('args: ', args)
    # print('config: ', config)

    if args.problem_char == "$":
        args.problem_char = config["contest_data"]["resent_problem_char"]
    else:
        with open("data/contest/contest_data.yml", "w") as f:
            config["contest_data"]["resent_problem_char"] = args.problem_char
            yaml.dump(config["contest_data"], f)

    if ord("a") <= ord(args.problem_char[0]) and ord(args.problem_char[0]) <= ord("z"):
        if len(args.problem_char) == 1:
            problem_number = ord(args.problem_char) - ord("a")
        else:
            problem_number = (ord(args.problem_char[0]) - ord("a") + 1) * 26 + (
                ord(args.problem_char[1]) - ord("a")
            )
    else:
        try:
            problem_number = int(args.problem_char)
        except:
            raise Exception("couldn't understand problem_char")

    with open("data/contest/problems.csv", encoding="utf-8_sig", mode="r") as f:
        problem = f.readlines()[problem_number].split(",")
        problem[2] = problem[2][:-1]

    if problem[0] == "atcoder":
        oj = AtCoder()
    elif problem[0] == "codeforces":
        oj = CodeForces()
    else:
        raise Exception(f"no such online judge: {problem[0]}")

    if args.source_path == "":
        source_path = config["source_path"]
    else:
        source_path = args.source_path

    pat = {}

    # predict
    pat["actual_arguments"], pat["formal_arguments"], pat["input_part"] = predict(
        oj.get_input(problem)
    )
    pat["yes_str"], pat["no_str"] = oj.get_auto_yn(problem)
    pat["mod"] = oj.get_mod(problem)

    # generate

    # output

    return
