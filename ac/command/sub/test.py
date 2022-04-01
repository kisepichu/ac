# coding: utf-8

import os
import subprocess
from command.sub.scripts import *
from command.sub.format_ans import format_ans


def test(config, problem):
    test_dir = f"data/testcase/atcoder/{problem[1]}/"
    if not os.path.exists(config["executable_path"]):
        return "CE", -1, 0

    results = []
    results_or = 0
    cnt = 0
    output_empty = 1
    while os.path.exists(test_dir + f"{problem[2]}_{cnt+1}.input"):
        cnt += 1

        result = "WJ"
        with open(
            test_dir + f"{problem[2]}_{cnt}.input", encoding="utf-8_sig", mode="r"
        ) as f:
            input = f.read()
        try:
            output = subprocess.run(
                config["execute"].split(),
                input=input.encode(),
                stdout=subprocess.PIPE,
                check=1,
                timeout=3,
            ).stdout.decode()
        except subprocess.CalledProcessError as e:
            result = "RE"
            results_or |= 4
            output = "(RE)"
        except subprocess.TimeoutExpired as e:
            result = "TLE"
            results_or |= 1
            output = "(TLE)"
        # proc = subprocess.Popen(config['execute'].split(), stdout=subprocess.PIPE)
        # output = proc.communicate(input)[0]
        # exit_code = proc.returncode

        with open(
            test_dir + f"{problem[2]}_{cnt}.output", encoding="utf-8_sig", mode="r"
        ) as f:
            expected = f.read()

        if result == "WJ":
            if format_ans(expected) != "":
                output_empty = 0
            if format_ans(expected) == format_ans(output):
                result = "AC"
            else:
                result = "WA"
                results_or |= 2

        print_case(cnt, input, expected, output, result)
        results.append(result)

    result = "WJ"
    if results_or >= 4:
        result = "RE"
    elif results_or >= 2:
        result = "WA"
    elif results_or >= 1:
        result = "TLE"
    else:
        result = "AC"

    print_summary(cnt, results)

    return result, cnt, output_empty
