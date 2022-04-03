# coding: utf-8

import os

cdots = [
    "\\cdots",
    "\\ldots",
    "\\dots",
    "...",
]
vdots = cdots + [
    "\\vdots",
    ":",
    "\\ddots",
]


def get_name_sub(s):
    r_name = s.find("_")
    if r_name == -1:
        return s, ""

    if s[r_name - 1] != "}":
        l_name = 0
    else:
        r_name -= 1
        l_name = r_name
        while s[l_name - 1] != "{":
            l_name -= 1
    l_sub = r_name + 1
    if s[l_sub] != "{":
        r_sub = l_sub + 1
    else:
        l_sub += 1
        r_sub = l_sub
        while s[r_sub] != "}":
            r_sub += 1
    return s[l_name:r_name], s[l_sub:r_sub]


def numeral(s):
    return ord("0") <= ord(s) and ord(s) <= ord("9")


def erasespaces(s):
    res = ""
    d = 0
    for c in s:
        if c == "{":
            d += 1
        elif c == "}":
            d -= 1
        if not d or c != " ":
            res += c
    return res


def make_sub(sub, dim):
    sub = sub.split(",")
    if sub[0] == "":
        sub = []
    ret = []
    if dim < 0:
        dim = len(sub)
        if dim == 1 and len(sub[0]) > 1 and numeral(sub[0][0]) and numeral(sub[0][1]):
            dim = len(sub[0])
    return sub, dim


def expand(ss, vars):
    ret = []

    # class
    varnum = 0
    varcharlist = 0
    for s in ss:
        ret.append({"class": "vdots"})
        if s == "":
            ret[-1]["class"] = "end"
            continue
        if (
            ord("a") <= ord(s[0])
            and ord(s[0]) <= ord("z")
            or ord("A") <= ord(s[0])
            and ord(s[0]) <= ord("Z")
        ):
            ret[-1]["class"] = "var"
            varnum += 1
            for pat in cdots:
                if pat in s:
                    ret[-1]["class"] = "var_charlist"
                    varcharlist = 1
                    break
        else:
            for pat in cdots:
                if pat in s:
                    ret[-1]["class"] = "cdots"
                    break
    if not varnum:
        for i in range(len(ss)):
            if ret[i]["class"] == "cdots":
                ret[i]["class"] = "vdots"
    if varcharlist:
        ret = ret[:1]
        ret[0]["class"] = "var_charlist"

    # name
    for i in range(len(ret)):
        if ret[i]["class"][:3] == "var":
            if ret[i]["class"] == "var_charlist":
                name, sub = get_name_sub(ss[i])
                sub = sub[:-1]
                vars[name] = {"dim": -1}
                ret[i]["name"] = name
                ret[i]["sub"], vars[name]["dim"] = make_sub(sub, vars[name]["dim"])
            elif ret[i]["class"] == "var":
                name, sub = get_name_sub(ss[i])
                if sub == "":
                    vars[name] = {"dim": -1}
                    ret[i]["name"] = name
                    ret[i]["sub"], vars[name]["dim"] = make_sub(sub, vars[name]["dim"])
                else:
                    if numeral(sub[0]) or name in vars.keys():
                        if name not in vars.keys():
                            vars[name] = {"dim": -1}
                        ret[i]["name"] = name
                        ret[i]["sub"], vars[name]["dim"] = make_sub(
                            sub, vars[name]["dim"]
                        )
                    else:
                        name = name + "_" + sub
                        vars[name] = {"dim": 0}
                        ret[i]["name"] = name
                        ret[i]["sub"] = ""

    return ret


def horizontal_reduction(ex):
    # print(ex)
    sub_size = len(ex[0]["sub"])
    mn = ["{"] * sub_size
    mx = ["/"] * sub_size
    for i in range(len(ex)):
        for j in range(sub_size):
            if ex[i]["class"] != "var":
                continue
            if ord(mn[j][0]) > ord(ex[i]["sub"][j][0]):
                mn[j] = ex[i]["sub"][j]
            if ord(mx[j][0]) < ord(ex[i]["sub"][j][0]):
                mx[j] = ex[i]["sub"][j]
    red = -1
    for j in range(sub_size):
        if mn[j] != mx[j]:
            red = j
    nex = ex[:1]
    if "size" not in nex[0]:
        nex[0]["size"] = []
    nex[0]["class"] = "var_vector"
    nex[0]["size"] += [mx[red] + "+1-(" + mn[red] + ")"]
    nex[0]["sub"] = ex[0]["sub"][:red] + ex[0]["sub"][red + 1 :]
    # print(nex)
    return nex


def read_sub(s, i, sd):
    if i > 0 and s[i - 1] == "{":
        l = i
        r = l + sd
        while r < len(s) and s[r] != "}":
            r += 1
        return s[l:r]
    else:
        return s[i : i + sd + 1]


def vertical_reduction(ex, times):
    # for es in ex:
    #     print(es)
    # print()
    nex = [
        [
            {
                "class": "rep",
                "loopvar": str(chr(ord("i") + times)),
                "begin": "1",
                "end": "",
            }
        ]
    ] + ex[1:2]
    times += 1

    if ex[1][0]["class"] != "vdots":
        for j in range(len(ex[0])):
            e = ex[0][j]
            if "sub" in e:
                for k in range(len(e["sub"])):
                    n = len(e["sub"][k])
                    for i in range(n):
                        dif = ord(ex[1][j]["sub"][k][i]) - ord(ex[0][j]["sub"][k][i])
                        if dif:
                            app = ""
                            start = ord(ex[0][j]["sub"][k][i]) - ord("1")
                            if start:
                                app = "+" + str(start)
                            nex[1][j]["sub"][k] = (
                                nex[1][j]["sub"][k][:i]
                                + nex[0][0]["loopvar"]
                                + app
                                + nex[1][j]["sub"][k][i + 1 :]
                            )
                            if nex[0][0]["end"] == "":
                                nex[0][0]["end"] = (
                                    read_sub(
                                        ex[-1][j]["sub"][k],
                                        i,
                                        len(ex[-1][j]["sub"][k])
                                        - len(ex[0][j]["sub"][k]),
                                    )
                                    + "+1-("
                                    + ex[0][j]["sub"][k][i]
                                    + ")"
                                )

            if "size" in e:
                for k in range(len(e["size"])):
                    n = len(e["size"][k])
                    for i in range(n):
                        dif = ord(ex[1][j]["size"][k][i]) - ord(ex[0][j]["size"][k][i])
                        if dif:
                            app = ""
                            start = ord(ex[0][j]["size"][k][i]) - ord("1")
                            if start:
                                app = "+" + str(start)
                            nex[1][j]["size"][k] = (
                                nex[1][j]["size"][k][:i]
                                + nex[0][0]["loopvar"]
                                + app
                                + nex[1][j]["size"][k][i + 1 :]
                            )
                            if nex[0][0]["end"] == "":
                                nex[0][0]["end"] = (
                                    read_sub(
                                        ex[-1][j]["sub"][k],
                                        i,
                                        len(ex[-1][j]["sub"][k])
                                        - len(ex[0][j]["size"][k]),
                                    )
                                    + "+1-("
                                    + ex[0][j]["size"][k][i]
                                    + ")"
                                )
    else:
        1

    return nex


def predict(problem, exs):
    success = ""
    v_times = 0

    # format, reduction
    vars = {}
    for ex in exs:
        ex = ex.split("\n")
        for i in range(len(ex)):
            print(ex[i].replace("\r", ""))
            ex[i] = expand(erasespaces(ex[i].replace("\r", "")).split(" "), vars)
        for i in range(len(ex)):
            if "name" in ex[i][-1].keys():
                vec_name = ex[i][-1]["name"]
                r = len(ex[i])
                l = r - 1
                while l >= 0 and (
                    ex[i][l]["class"] == "cdots"
                    or "name" in ex[i][l]
                    and ex[i][l]["name"] == vec_name
                ):
                    l -= 1
                l += 1
                if r - l > 2:
                    ex[i] = ex[i][0:l] + horizontal_reduction(ex[i][l:r])
            # print(ex[i])
        # print()
        nex = []
        l = 0
        while l < len(ex) and ex[l][0]["class"] != "end":
            r = l
            while r < len(ex) and (
                ex[r][0]["class"] == "vdots"
                or "name" in ex[l][0]
                and "name" in ex[r][0]
                and ex[l][0]["name"] == ex[r][0]["name"]
            ):
                r += 1
            if r - l > 1:
                nex += vertical_reduction(ex[l:r], v_times)
            else:
                nex += ex[l:r]
            l = r
        for ne in nex:
            print(ne)

    # get testcases
    test_dir = f"data/testcase/atcoder/{problem[1]}/"
    tests = []
    cnt = 0
    while os.path.exists(test_dir + f"{problem[2]}_{cnt+1}.input"):
        cnt += 1
        with open(
            test_dir + f"{problem[2]}_{cnt}.input", encoding="utf-8_sig", mode="r"
        ) as f:
            tests += {"cur": 0, "raw": f.read().replace("\r", "").split("\n")}

    print(vars)

    # type

    return success, "a", "a", "a"
