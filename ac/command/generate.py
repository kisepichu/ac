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

    pat = {}

    # predict
    (
        pat["prediction_success"],
        pat["actual_arguments"],
        pat["formal_arguments"],
        pat["input_part"],
    ) = predict(problem, oj.get_input(problem))
    pat["yes_str"], pat["no_str"] = oj.get_auto_yn(problem)
    pat["mod"] = oj.get_mod(problem)

    # generate
    template = []
    with open(config["template_path"], encoding="utf-8_sig", mode="r") as f:
        template = f.read()
    template = template.split("\n")
    source = []

    commands = ["pass"]
    ifs = []
    elses = []
    elsefs = []
    conds = []
    ok = 1
    for i in range(len(template)):
        line = template[i]
        for k, v in pat.items():
            line = line.replace("{{ " + k + " }}", v)
            line = line.replace("{{" + k + "}}", v)

        if line.startswith("{%"):
            tmp = line.split()
            if tmp[1] == "if":
                commands.append("if")
                ifs.append([])
                elses.append([])
                elsefs.append(0)
                conds.append(tmp[2])
            elif tmp[1] == "else":
                elsefs[-1] = 1
            elif tmp[1] == "endif":
                commands.pop()
                if pat[conds[-1]] != "":
                    source += ifs[-1]
                else:
                    source += elses[-1]
                ifs.pop()
                elses.pop()
                elsefs.pop()
                conds.pop()
        else:
            if commands[-1] == "pass":
                source += [line]
            elif commands[-1] == "if":
                if elsefs[-1]:
                    elses[-1] += [line]
                else:
                    ifs[-1] += [line]

    # with open(config["source_path"], mode="w") as f:
    #     f.write("\n".join(source))
    #     1

    return
