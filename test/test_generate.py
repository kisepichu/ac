# coding: utf-8

test_str = "998244353"
wait = 0

import os
import sys
import yaml
import time
import pytest
from urllib.parse import urlparse

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath("../ac"))

from command.generate import *
from command.comp import *
from command.run import *


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

    def __init__(self, n, problem_id):
        self.testcase_num = n
        self.problem_char = problem_id


urls = []
config = {}

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/ac")
with open("../test/data/test_problems.yml", encoding="utf-8_sig", mode="r") as f:
    urls = yaml.safe_load(f)["generate"]
with open("config.yml", encoding="utf-8_sig", mode="r") as f:
    config = yaml.safe_load(f)
with open("data/contest/contest_data.yml", encoding="utf-8_sig", mode="r") as f:
    config["contest_data"] = yaml.safe_load(f)

config["test_generate"] = "\n\tlin(n9982);out(n9982);"
config["run_input"] = "\n" + test_str + "\n"
config["run_no_print_case"] = 1


# @pytest.fixture(autouse=True)
# def fixture():
#     print("b")
#     os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/ac")
#     with open("../test/data/test_problems.yml", encoding="utf-8_sig", mode="r") as f:
#         urls = yaml.safe_load(f)["generate"]
#     with open("config.yml", encoding="utf-8_sig", mode="r") as f:
#         config = yaml.safe_load(f)
#     with open("data/contest/contest_data.yml", encoding="utf-8_sig", mode="r") as f:
#         config["contest_data"] = yaml.safe_load(f)
#     oj = AtCoder()

#     config["test_generate"] = "\n\tlin(n9982);out(n9982);"
#     config["run_input"] = "\n" + test_str + "\n"
#     print("c", urls)
#     return urls


@pytest.mark.parametrize("urlnum", [i for i in range(len(urls))])
def test_inputsize(urlnum):
    global oj
    global urls
    global config
    url = urls[urlnum]
    if not url.startswith("http"):
        url = "https://atcoder.jp/contests/" + url

    time.sleep(wait)
    generate(generate_args(url.split("/")[-1]), config)
    comp(comp_args(), config)
    ok = 1
    testcase_num = 1
    while 1:
        try:
            output = run(run_args(testcase_num, url.split("/")[-1]), config)
        except:
            break
        assert output == test_str + "\n"
        testcase_num += 1
    testcase_num -= 1
    assert testcase_num > 0
