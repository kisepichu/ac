# coding: utf-8

import requests
import re
import urllib
import os
import sys
import lxml.html
import time
from datetime import datetime


class AtCoder:
    LOGIN_URL = "https://atcoder.jp/login"

    def __init__(self):
        self.get_session()
        return

    def get_session(self):
        self.session = requests.Session()
        self.res = self.session.get(self.LOGIN_URL)
        self.url = self.LOGIN_URL
        self.tree = lxml.html.fromstring(self.res.text)
        self.csrf_token = self.tree.xpath('//*[@name="csrf_token"]/@value')[0]
        payload = {
            "username": os.environ.get("ac_id"),
            "password": os.environ.get("ac_password"),
            "csrf_token": self.csrf_token,
        }
        self.session.post(self.LOGIN_URL, data=payload)
        return

    def get_statement_a(self, contest_id, f5=0):
        if self.url != f"https://atcoder.jp/contests/{contest_id}/tasks_print?lang=ja":
            self.url = f"https://atcoder.jp/contests/{contest_id}/tasks_print?lang=ja"
            self.res = self.session.get(
                f"https://atcoder.jp/contests/{contest_id}/tasks_print?lang=ja"
            )

        if f5:
            while self.res.status_code != 200:
                print(self.res.status_code)
                time.sleep(0.5)
                self.res = self.session.get(
                    f"https://atcoder.jp/contests/{contest_id}/tasks_print?lang=ja"
                )
        else:
            if self.res.status_code != 200:
                self.url = ""
                raise Exception(
                    f"status_code {self.res.status_code}: https://atcoder.jp/contests/{contest_id}/tasks_print?lang=ja"
                )

        self.tree = lxml.html.fromstring(self.res.text)
        statementx = self.tree.xpath(
            f'/html/body/div[@id="main-div"]/div[@id="main-container"]/div[@class="row"]/div[@class="col-sm-12"][1]/div[@id="task-statement"]/span[@class="lang"]/span[@class="lang-ja"]/div[@class="part"][1]/section'
        )
        inputx = self.tree.xpath(
            f'/html/body/div[@id="main-div"]/div[@id="main-container"]/div[@class="row"]/div[@class="col-sm-12"][1]/div[@id="task-statement"]/span[@class="lang"]/span[@class="lang-ja"]/div[@class="io-style"]/div[@class="part"][1]/section'
        )
        insamplex = self.tree.xpath(
            f"/html/body/div[@id='main-div']/div[@id='main-container']/div[@class='row']/div[@class='col-sm-12']/div[@id='task-statement']/span[@class='lang']/span[@class='lang-ja']/div[@class='part'][3]/section"
        )
        outsamplex = self.tree.xpath(
            f"/html/body/div[@id='main-div']/div[@id='main-container']/div[@class='row']/div[@class='col-sm-12']/div[@id='task-statement']/span[@class='lang']/span[@class='lang-ja']/div[@class='part'][4]/section"
        )

        statement = statementx[0].text_content()[5:]
        statement += "in.\n" + inputx[0][2].text_content()
        statement += (
            "ex.\n"
            + insamplex[0][1].text_content()
            + "  ->  "
            + outsamplex[0][1].text_content()
        )

        return statement

    def get_problems(self, contest_id, f5=0):
        if self.url != f"https://atcoder.jp/contests/{contest_id}/submit":
            self.url = f"https://atcoder.jp/contests/{contest_id}/submit"
            self.res = self.session.get(
                f"https://atcoder.jp/contests/{contest_id}/submit"
            )
        if f5:
            while self.res.status_code != 200:
                print(self.res.status_code)
                time.sleep(0.5)
                self.res = self.session.get(
                    f"https://atcoder.jp/contests/{contest_id}/submit"
                )
        else:
            if self.res.status_code != 200:
                self.url = ""
                raise Exception(
                    f"status_code {self.res.status_code}: https://atcoder.jp/contests/{contest_id}/submit"
                )

        self.tree = lxml.html.fromstring(self.res.text)
        problem_ids = self.tree.xpath('//*[@id="select-task"]/option/@value')
        problems = []
        for problem_id in problem_ids:
            problems.append(["atcoder", contest_id, problem_id])
        return problems

    def get_start_time(self, contest_id):
        if self.url != f"https://atcoder.jp/contests/{contest_id}":
            self.url = f"https://atcoder.jp/contests/{contest_id}"
            self.res = self.session.get(f"https://atcoder.jp/contests/{contest_id}")
        self.tree = lxml.html.fromstring(self.res.text)
        start_str = self.tree.xpath('//*[@class="fixtime fixtime-full"]')[
            0
        ].text_content()
        # start_str = '2020-6-27 2:37:00+0900'
        return datetime.strptime(start_str[:-5], "%Y-%m-%d %H:%M:%S")

    def get_contest_id(self, url):
        urlpath = url.path[1:].split("/")
        if len(urlpath) >= 2 and urlpath[0] == "contests":
            return urlpath[1]
        else:
            return None

    def see_problem(self, problem):
        if (
            self.url
            != f"https://atcoder.jp/contests/{problem[1]}/tasks/{problem[2]}?lang=ja"
        ):
            self.url = (
                f"https://atcoder.jp/contests/{problem[1]}/tasks/{problem[2]}?lang=ja"
            )
            self.res = self.session.get(
                f"https://atcoder.jp/contests/{problem[1]}/tasks/{problem[2]}?lang=ja"
            )
            if self.res.status_code != 200:
                self.url = ""
                raise Exception(
                    f"status_code {self.res.status_code}: https://atcoder.jp/contests/{problem[1]}/tasks/{problem[2]}?lang=ja"
                )
            self.tree = lxml.html.fromstring(self.res.text)

    def get_input(self, problem):
        self.see_problem(problem)

        elem = self.tree.xpath(f'//h3[text()="入力"]')[0]
        res = []
        while elem is not None:
            if elem.tag == "pre":
                s = ""
                for t in elem.itertext():
                    s += t
                res += [s]
            elem = elem.getnext()
        # print(res)
        return res

    def get_auto_yn(self, problem):
        self.see_problem(problem)

        yns = [
            ["yes", "no"],
            ["Yes", "No"],
            ["YES", "NO"],
            ["possible", "impossible"],
            ["Possible", "Impossible"],
            ["Yay!", ":("],
            ["POSSIBLE", "IMPOSSIBLE"],
            ["Takahashi", "Aoki"],
        ]

        elem = self.tree.xpath(f'//h3[text()="出力"]')[0].getparent()
        s = ""
        for t in elem.itertext():
            s += t
        found = set()
        for i in range(len(yns)):
            yn = yns[i]
            if yn[0] in s or yn[1] in s:
                found.add(i)
        res_yes = ""
        res_no = ""
        if len(found) == 1:
            for i in found:
                res_yes = yns[i][0]
                res_no = yns[i][1]

        # print(res_yes, res_no)
        return res_yes, res_no

    def get_mod(self, problem):
        self.see_problem(problem)

        mods = {
            "998244353": 998244353,
            "1000000007": 1000000007,
            "1000000009": 1000000009,
            "1e9+7": 1000000007,
            "1e9 + 7": 1000000007,
            "10^9+7": 1000000007,
            "10^9 + 7": 1000000007,
            "1e9+9": 1000000009,
            "1e9 + 9": 1000000009,
            "10^9+9": 1000000009,
            "10^9 + 9": 1000000009,
        }

        elem = self.tree.xpath(f'//h3[text()="問題文"]')[0].getparent()
        s = ""
        for t in elem.itertext():
            s += t
        found = set()
        for sign, mod in mods.items():
            if sign in s:
                found.add(mod)
        ret = ""
        if len(found) == 1:
            for mod in found:
                ret = str(mod)
        # print(ret)
        return ret

    def download_testcases(self, problem):
        test_dir = f"data/testcase/atcoder/{problem[1]}/"
        if os.path.exists(test_dir + f"{problem[2]}_1.input"):
            return -1
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)

        self.see_problem(problem)

        cnt = 0
        while len(self.tree.xpath(f'//h3[text()="入力例 {cnt+1}"]')):
            cnt += 1

            input_data = self.tree.xpath(f'//h3[text()="入力例 {cnt}"]')[0].getnext().text
            output_data = self.tree.xpath(f'//h3[text()="出力例 {cnt}"]')[0].getnext().text

            if input_data is None:
                continue

            with open(test_dir + f"{problem[2]}_{cnt}.input", mode="w") as f:
                for line in input_data:
                    f.write(line)

            if output_data is None:
                continue

            with open(test_dir + f"{problem[2]}_{cnt}.output", mode="w") as f:
                for line in output_data:
                    f.write(line)

        return cnt

    def submit(self, problem, language_id, source):
        payload = {
            "data.TaskScreenName": problem[2],
            "data.LanguageId": language_id,
            "sourceCode": source,
            "csrf_token": self.csrf_token,
        }
        # print(payload)
        return self.session.post(
            f"https://atcoder.jp/contests/{problem[1]}/submit", data=payload
        ).content
