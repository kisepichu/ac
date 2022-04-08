# coding: utf-8

import os
import subprocess
from command.sub.format import format


def comp(args, config):
    if args.source_path == "":
        source_path = config["source_path"]
    else:
        source_path = args.source_path

    # format
    with open(source_path, encoding="utf-8_sig", mode="r") as f:
        source = f.read()
    if not args.no_format:
        with open(config["formatted_path"], mode="w+") as f:
            source = format(source)
            f.write(source)
        source_path = config["formatted_path"]

    # compile
    if os.path.exists(config["executable_path"]):
        os.remove(config["executable_path"])
    subprocess.run(config["compile"].replace("{{source}}", source_path).split())
    return
