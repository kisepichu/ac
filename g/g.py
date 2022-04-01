# coding: utf-8

import sys
import os
import subprocess
import argparse
import yaml

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pat = [
    ["    ", "	"],
    ["long long", "lint"],
    ["std::", ""],
]

pat2 = [
    ["    ", "	"],
]


def main():
    # for arg in sys.argv:
    #    print(arg)

    with open("../ac/config.yml", encoding="utf-8_sig", mode="r") as f:
        config = yaml.safe_load(f)

    parser = argparse.ArgumentParser(description="perf +100")
    parser.add_argument("problem_char", help="a-z")
    args = parser.parse_args()

    with open(
        "../ac/data/contest/contest_data.yml", encoding="utf-8_sig", mode="r"
    ) as f:
        contest_data = yaml.safe_load(f)
    contest_data["resent_problem_char"] = args.problem_char
    with open("../ac/data/contest/contest_data.yml", "w") as f:
        yaml.dump(contest_data, f)

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

    with open("../ac/data/contest/problems.csv", encoding="utf-8_sig", mode="r") as f:
        problem = f.readlines()[problem_number].split(",")
        problem[2] = problem[2][:-1]

    if problem[0] == "atcoder":
        url = f"https://atcoder.jp/contests/{problem[1]}/tasks/{problem[2]}"
    elif problem[0] == "codeforces":
        url = f"https://codeforces.com/contest/{problem[1]}/problem/{problem[2]}"

    if not os.path.exists(f"auto/{problem[1]}"):
        print(
            f'atcoder-tools gen {problem[1]} --workspace auto --template {config["template_path"]}'
        )
        subprocess.run(
            f'atcoder-tools gen {problem[1]} --workspace auto --template {config["template_path"]}'.split(),
            stdout=subprocess.PIPE,
        ).stdout.decode().split("\n")
        # print("a")

    print(problem[2])
    if os.path.exists(f"auto/{problem[1]}/{problem[2][-1].upper()}/main.cpp"):
        path = f"auto/{problem[1]}/{problem[2][-1].upper()}/main.cpp"
    else:  # typical90
        if problem[2][-2] == "_":
            k = ord(problem[2][-1]) - ord("a")
        else:
            k = (ord(problem[2][-2]) - ord("a") + 1) * 26 + (
                ord(problem[2][-1]) - ord("a")
            )
        k += 1
        st = str(k).zfill(3)
        path = f"auto/{problem[1]}/{st}/main.cpp"
    with open(path) as f:
        output = f.readlines()

    sta = ["root"]
    with open("../example.cpp", mode="w") as f:
        output_flag = 0
        for line in output:
            if line.startswith("#pragma region"):
                s = line.split()
                sta.append(s[2])
            if line.startswith("#pragma endregion"):
                sta.pop()
            if sta[-1] == "main" or sta[-1] == "solve":
                # print("a")
                for p in pat:
                    line = line.replace(p[0], p[1])
                if line.startswith("int solve"):
                    line = line.lower()
            for p in pat2:
                line = line.replace(p[0], p[1])
            f.write(line)


if __name__ == "__main__":
    main()
