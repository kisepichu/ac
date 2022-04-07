# coding: utf-8

test_str = "998244353"
wait = 0.3

import os
import sys
import yaml
import time
from urllib.parse import urlparse

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath("../ac"))

from command.oj.atcoder import AtCoder
from command.oj.codeforces import CodeForces
from command.oj.atcoderproblems import AtCoderProblems
from command.generate import *
from command.comp import *
from command.run import *

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/ac")


class generate_args:
    problem_char = "$"

    def __init__(self, problem_id):
        self.problem_char = problem_id


class comp_args:
    source_path = ""
    no_format = False


class run_args:
    problem_char = "$"
    testcase_num = 0
    add_input = True

    def __init_(self, n):
        testcase_num = n


def main():
    with open("../test/data/test_problems.yml", encoding="utf-8_sig", mode="r") as f:
        urls = yaml.safe_load(f)["generate"]
    with open("config.yml", encoding="utf-8_sig", mode="r") as f:
        config = yaml.safe_load(f)
    with open("data/contest/contest_data.yml", encoding="utf-8_sig", mode="r") as f:
        config["contest_data"] = yaml.safe_load(f)

    oj = AtCoder()

    for url in urls:
        if not url.startswith("http"):
            url = "https://atcoder.jp/contests/" + url
        urlp = urlparse(url)
        if urlp.netloc == "atcoder.jp" and type(oj) != AtCoder:
            oj = AtCoder()
        elif urlp.netloc == "codeforces.com" and type(oj) != CodeForces:
            oj = CodeForces()
        elif urlp.netloc == "kenkoooo.com" and type(oj) != AtCoderProblems:
            oj = AtCoderProblems()

        config["test_generate"] = "\n\tlin(n9982);out(n9982);"
        config["run_input"] = "\n" + test_str + "\n"
        generate(generate_args(url.split("/")[-1]), config)
        comp(comp_args(), config)
        ok = 1
        c = 1
        while 1:
            try:
                output = run(run_args(c), config)
            except:
                break
            if output != test_str:
                ok = 0
            c += 1
        if not ok:
            print("FAIL: " + url)
            exit(1)
        else:
            print(" OK : " + url)
        time.sleep(wait)


if __name__ == "__main__":
    main()
