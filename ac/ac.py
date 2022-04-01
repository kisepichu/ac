# coding: utf-8

from command.abca import *
from command.make_snippets import *
from command.clear import *
from command.cpy import *
from command.submit import *
from command.comp import *
from command.run import *
from command.init import *
import sys
import os
import argparse
import yaml

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    with open("config.yml", encoding="utf-8_sig", mode="r") as f:
        config = yaml.safe_load(f)
    with open("data/contest/contest_data.yml", encoding="utf-8_sig", mode="r") as f:
        config["contest_data"] = yaml.safe_load(f)

    parser = argparse.ArgumentParser(description="")
    subparsers = parser.add_subparsers()

    # init
    parser_init = subparsers.add_parser("init")
    parser_init.add_argument("contest_url", help="atcoder, ")
    parser_init.add_argument(
        "-d",
        "--download",
        action="store_false",
        help="download testcases when the contest starts",
    )
    parser_init.add_argument(
        "-a",
        "--show-a",
        action="store_true",
        help="show the statement of problem a when the contest starts",
    )
    parser_init.set_defaults(handler=init)

    # submit
    parser_submit = subparsers.add_parser("submit")
    parser_submit.add_argument(
        "-c", "--choose", action="store_true", help="choose whether to submit"
    )
    parser_submit.add_argument("-f", "--force", action="store_true", help="")
    parser_submit.add_argument("-p", "--compile", default="", help="compile command")
    parser_submit.add_argument("-s", "--source_path", default="", help="source path")
    parser_submit.add_argument(
        "-n", "--no_format", action="store_true", help="no format"
    )
    parser_submit.add_argument("problem_char", nargs="?", default="$")
    parser_submit.set_defaults(handler=submit)

    # copy
    parser_copy = subparsers.add_parser("copy")
    parser_copy.add_argument("-s", "--source_path", default="", help="source path")
    parser_copy.add_argument("-n", "--no_format", action="store_true", help="no format")
    parser_copy.set_defaults(handler=cpy)

    # clear
    parser_clear = subparsers.add_parser("clear")
    parser_clear.set_defaults(handler=clear)

    # compile
    parser_compile = subparsers.add_parser("compile")
    parser_compile.add_argument("-s", "--source_path", default="", help="source path")
    parser_compile.add_argument(
        "-n", "--no_format", action="store_true", help="no format"
    )
    parser_compile.set_defaults(handler=comp)

    # run
    parser_run = subparsers.add_parser("run")
    parser_run.add_argument(
        "testcase_num",
        type=int,
        nargs="?",
        default=-1,
        help="empty to just run, 0 to paste from clipboard",
    )
    parser_run.add_argument("problem_char", nargs="?", default="$")
    parser_run.set_defaults(handler=run)

    # make-snippets
    parser_make_snippets = subparsers.add_parser("make-snippets")
    parser_make_snippets.set_defaults(handler=make_snippets)

    # abca
    parser_abca = subparsers.add_parser("abca")
    parser_abca.add_argument("-i", "--input", action="store_false")
    parser_abca.add_argument("-p", "--problem_char", help="a-z")
    parser_abca.set_defaults(handler=abca)

    args = parser.parse_args()
    if hasattr(args, "handler"):
        args.handler(args, config)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
