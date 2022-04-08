# coding: utf-8

import yaml


def complement_problem_char(args, config):
    contest_id = ""
    if len(args.problem_char) > 3:
        contest_id = "".join(args.problem_char.split("_")[:-1])
        args.problem_char = "".join(args.problem_char.split("_")[-1:])
        # print(contest_id, args.problem_char)

    if args.problem_char == "$":
        args.problem_char = config["contest_data"]["resent_problem_char"]
    else:
        config["contest_data"] = {"resent_problem_char": "a"}
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
    return contest_id, problem_number
