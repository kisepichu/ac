# coding: utf-8

import os
import copy

cdots = [
    "\\cdots",
    "\\ldots",
    "\\dots",
    "...",
    "..",
]
vdots = cdots + [
    "\\vdots",
    ":",
    "\\ddots",
]


def get_name_sub(s):
    # print(s)
    # ubarpos = s.find("_")
    ubarpos = -1
    inparen = 0
    for i in range(len(s)):
        if s[i] == "{":
            inparen += 1
        if not inparen and s[i] == "_":
            ubarpos = i
        if s[i] == "}":
            inparen -= 1
    # print(ubarpos)
    r_name = ubarpos
    if r_name == -1:
        return s, ""

    if s[r_name - 1] != "}":
        l_name = 0
    else:
        r_name -= 1
        l_name = r_name
        while l_name - 1 >= 0 and s[l_name - 1] != "{":
            l_name -= 1
    l_sub = ubarpos + 1
    if s[l_sub] != "{":
        r_sub = l_sub + 1
    else:
        l_sub += 1
        r_sub = l_sub
        while r_sub < len(s) and s[r_sub] != "}":
            r_sub += 1
    return s[l_name:r_name], s[l_sub:r_sub]


def numeral(s):
    return ord("0") <= ord(s) and ord(s) <= ord("9")


def alphabet(s):
    return (
        ord("a") <= ord(s)
        and ord(s) <= ord("z")
        or ord("A") <= ord(s)
        and ord(s) <= ord("Z")
    )


def lparen(s):
    return s == "{" or s == "("


def rparen(s):
    return s == "}" or s == ")"


def erasespaces(s):
    s = s.replace("  ", " ").replace("  ", " ").replace("  ", " ")
    res = ""
    d = 0
    rms = ["\\mathrm", "\\rm", "\\text", "\\textrm"]
    for rm in rms:
        s = s.replace("{" + rm, rm + "{")
    for rm in rms:
        pos = s.find(rm)
        if pos != -1:
            s = s.replace(rm, "")
            s = s.replace(" ", "_", 1)
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
            # ret.pop()
            ret[-1]["class"] = "empty"
            continue
        if numeral(s[0]):
            ret[-1]["class"] = "query_type"
            ret[-1]["num"] = s[0]
        elif alphabet(s[0]) or lparen(s[0]):
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
    query_region = 0
    for i in range(len(ret)):
        if ret[i]["class"] == "query_type":
            query_region = 1
        if ret[i]["class"][:3] == "var":
            if ret[i]["class"] == "var_charlist":
                name, sub = get_name_sub(ss[i])
                name = name[0]
                sub = sub[:-1]
                vars[name] = {"dim": -1, "type": -10}
                ret[i]["name"] = name
                ret[i]["sub"], vars[name]["dim"] = make_sub(sub, vars[name]["dim"])
                vars[name]["dim"] += 1
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
                    elif query_region:
                        if sub[0] != "i":
                            name = name + "_" + sub
                        if name not in vars.keys():
                            vars[name] = {"dim": 1, "vertical_reducted": 1}
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
    mn = ["{{{{"] * sub_size
    mx = ["/"] * sub_size
    for i in [0, -1]:
        for j in range(sub_size):
            if ex[i]["class"] != "var":
                continue
            if len(mn[j]) > len(ex[i]["sub"][j]) and mn[j] > ex[i]["sub"][j]:
                mn[j] = ex[i]["sub"][j]
            if len(mx[j]) < len(ex[i]["sub"][j]) or mx[j] < ex[i]["sub"][j]:
                mx[j] = ex[i]["sub"][j]
    red = sub_size - 1
    for j in range(sub_size):
        if mn[j] != mx[j]:
            red = j
    nex = ex[:1]
    if "size" not in nex[0]:
        nex[0]["size"] = []
    nex[0]["class"] = "var_vector"
    nex[0]["size"] += [mx[red] + ("+1" if mn[red] == "0" else "")]
    nex[0]["horizontal_offset"] = [mn[red]]
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


def vertical_reduction(ex, times, vars):
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
    ]
    times += 1

    if ex[1][0]["class"] == "vdots":
        # print(ex)
        eins = copy.deepcopy(ex[0])
        for j in range(len(eins)):
            for key in ["sub", "size", "horizontal_offset"]:
                if key in eins[j]:
                    for k in range(len(eins[j][key])):
                        n = len(eins[j][key][k])
                        for i in range(n):
                            dif = ord(ex[-1][j][key][k][i]) - ord(ex[0][j][key][k][i])
                            if dif:
                                eins[j][key][k] = (
                                    eins[j][key][k][:i]
                                    + str(chr(ord(eins[j][key][k][i]) + 1))
                                    + eins[j][key][k][i + 1 :]
                                )
        ex = ex[:1] + [eins] + ex[1:]
    nex += ex[1:2]
    for j in range(len(nex[1])):
        vars[nex[1][j]["name"]]["vertical_reducted"] = 1
    for j in range(len(ex[0])):
        e = ex[0][j]
        for key in ["sub", "size", "horizontal_offset"]:
            if key in e:
                for k in range(len(e[key])):
                    n = len(e[key][k])
                    for i in range(n):
                        dif = ord(ex[1][j][key][k][i]) - ord(ex[0][j][key][k][i])
                        if dif:
                            app = ""
                            start = ord(ex[0][j][key][k][i]) - ord("1")
                            if start:
                                app = "+" + str(start)
                            nex[1][j][key][k] = (
                                nex[1][j][key][k][:i]
                                + nex[0][0]["loopvar"]
                                + app
                                + nex[1][j][key][k][i + 1 :]
                            )
                            if nex[0][0]["end"] == "":
                                nex[0][0]["end"] = (
                                    read_sub(
                                        ex[-1][j][key][k],
                                        i,
                                        len(ex[-1][j][key][k]) - len(ex[0][j][key][k]),
                                    )
                                    + "+1-("
                                    + ex[0][j][key][k][i]
                                    + ")"
                                )

    return nex


def guess(vars, constraint):
    constraint = erasespaces(constraint)
    ne = ""
    paren = 0
    for c in constraint:
        if lparen(c):
            paren += 1
        if paren == 0:
            ne += c
        else:
            ne += c.replace(",", "$")
        if rparen(c):
            paren -= 1
    constraint = ne
    constraint = (
        constraint.replace("\\", " \\").replace("  ", " ").replace(",", " ").split(" ")
    )
    change = set()

    for i in range(len(constraint)):
        if "入力は全て整数" in constraint[i] or "入力はすべて整数" in constraint[i]:
            for var, d in vars.items():
                d["type"] += 2.5
            return

    constraint_type = ""
    strength = 2

    for i in range(len(constraint) - 1, -1, -1):
        constraint[i] = constraint[i].replace("$", ",")
        if constraint_type == "":
            if "文字列" in constraint[i]:
                constraint_type = "str"
                strength = 3
            elif "整数" in constraint[i]:
                constraint_type = "int"
                strength = 3
            elif "英小文字" in constraint[i] or "英大文字" in constraint[i]:
                constraint_type = "str"
                strength = 4
            elif "数字" in constraint[i]:
                constraint_type = "str"
        if constraint_type == "":
            try:
                n = int(
                    eval(
                        constraint[i]
                        .replace("^", "**")
                        .replace("{", "")
                        .replace("}", "")
                    )
                )
                if n > 10**20:
                    constraint_type = "str"
                    strength = 4
            except:
                1
        if constraint_type == "":
            if (
                "\\leq" in constraint[i]
                or "\\leqq" in constraint[i]
                or "\\le" in constraint[i]
                or "\\times" in constraint[i]
                or "<" in constraint[i]
                or "≤" in constraint[i]
            ):
                constraint_type = "int"
                strength = 4
            elif constraint[i] == "#" or constraint[i] == ".":
                constraint_type = "str"
        name, sub = get_name_sub(constraint[i])
        if name + "_" + sub in vars.keys():
            change.add(name + "_" + sub)
        if name in vars.keys():
            change.add(name)
    # print(constraint)
    # print(constraint_type)
    # print(change)
    # print()
    if constraint_type == "int":
        for e in change:
            vars[e]["type"] += strength
    elif constraint_type == "str":
        for e in change:
            vars[e]["type"] -= strength

    return


def convert_sub(s):
    if "_" in s:
        l = s.split("_")

        l[0] = l[0].replace("{", "").replace("}", "")
        if l[1][0] != "{":
            l[1] = "{" + l[1] + "}"
        l[1] = l[1].replace("{", "[").replace("}", "]")
        s = "".join(l)

    f = set()
    for i in range(len(s) - 1):
        if numeral(s[i]) and alphabet(s[i + 1]):
            f.add(i)
    d = 0
    for e in f:
        s = s[: e + d + 1] + "*" + s[e + d + 1 :]
        d += 1

    return s


def predict(problem, exs, constraints):

    # format, reduction
    v_times = 0
    vars = {}
    for ex_i in range(len(exs)):
        ex = exs[ex_i]
        ex = ex.split("\n")
        for i in range(len(ex)):
            # print(erasespaces(ex[i].replace("\r", "")))
            ex[i] = expand(erasespaces(ex[i].replace("\r", "")).split(" "), vars)
            # print(ex[i])
        for i in range(len(ex)):
            if "name" in ex[i][-1].keys():
                vec_name = ex[i][-1]["name"]
                r = len(ex[i])
                l = r - 1
                while l >= 0 and (
                    ex[i][l]["class"] == "cdots"
                    or ex[i][l]["class"] == "empty"
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
        fnames = []
        while l < len(ex):
            r = l + 1
            while r < len(ex):
                if "name" in ex[r - 1][0]:
                    fnames += [ex[r - 1][0]["name"]]
                else:
                    ok = 0
                    for j in range(len(ex[r - 1])):
                        ok |= ex[r - 1][j]["class"] == "vdots"
                    if ok:
                        ex[r - 1][0]["class"] = "vdots"
                if ex[r - 1][0]["class"] == "vdots":
                    nname = ex[r][0]["name"]
                    while ex[l][0]["name"] != nname:
                        nex += ex[l : l + 1]
                        l += 1
                    laststart = r
                    c = 0
                    while (
                        "name" in ex[l + c][0]
                        and "name" in ex[r][0]
                        and ex[l + c][0]["name"] == ex[r][0]["name"]
                    ):
                        r += 1
                        c += 1
                    lumpsize = r - laststart
                    pas = []
                    while ex[l][0]["class"] != "vdots":
                        for i in range(1, lumpsize):
                            ex[l] += ex[l + i]
                        pas += [ex[l]]
                        l += lumpsize
                    pas += [ex[l]]
                    l += 1
                    for i in range(1, lumpsize):
                        ex[l] += ex[l + i]
                    pas += [ex[l]]
                    nex += vertical_reduction(pas, v_times, vars)
                    l = r
                r += 1
            if r >= len(ex):
                for i in range(l, r):
                    nex += ex[i : i + 1]
                break

        exs[ex_i] = nex

    # input type

    if len(exs) == 1:
        input_type = "normal"
    elif exs[1][0][0]["class"] == "query_type":
        input_type = "queries"
    else:
        input_type = "testcases"

    if input_type == "queries":
        query_vars = set(["q_type"])
        vars["q_type"] = {"dim": 1, "type": 10}
        for i in range(len(exs[0]) - 2, -1, -1):
            if exs[0][i][0]["class"] == "rep" and exs[0][i + 1][0]["class"] == "var":
                exs[0][i + 1][0]["class"] = "query"
                if exs[0][i + 1][0]["name"] in vars.keys():
                    vars.pop(exs[0][i + 1][0]["name"])
                break
        for ex_i in range(1, len(exs)):
            ex = exs[ex_i]
            for es_i in range(len(ex)):
                es = ex[es_i]
                for e in es:
                    if (
                        e["class"] == "var"
                        or e["class"] == "var_vector"
                        or e["class"] == "var_charlist"
                    ):
                        if vars[e["name"]]["dim"] == 0:
                            vars[e["name"]]["dim"] = 1
                        e["sub"] = ["i"]

    # get testcases

    # test_dir = f"data/testcase/atcoder/{problem[1]}/"
    # tests = []
    # cnt = 0
    # while os.path.exists(test_dir + f"{problem[2]}_{cnt+1}.input"):
    #     cnt += 1
    #     with open(
    #         test_dir + f"{problem[2]}_{cnt}.input", encoding="utf-8_sig", mode="r"
    #     ) as f:
    #         tests += {"cur": 0, "raw": f.read().replace("\r", "").split("\n")}

    # type

    for var, d in vars.items():
        if "type" not in d:
            d["type"] = 0
        if var == "S":
            d["type"] -= 1
        if var == "T" and "S" in vars.keys():
            d["type"] -= 0.4

    for constraint in constraints:
        guess(vars, constraint)

    # lower
    # tolower = set()
    # for var, d in vars.items():
    #     if var[0].isupper() and var.lower() not in vars.keys():
    #         tolower.add(var)
    # for e in tolower:
    #     vars[e.lower()] = vars[e]
    #     vars.pop(e)
    # print(vars)

    # cppify

    success = "1"
    aargs = ""  # n, m, a
    fargs = ""  # int n, int m, vector<vector<lint>> a
    input_part = [""] * len(exs)  # vector<vector<lint>> a(h)

    indent = 1

    def vector_lint(n):
        if n <= 0:
            return "lint"
        return "vector<" + vector_lint(n - 1) + ">"

    def vector_cs(n):
        if n <= 1:
            return "cs"
        return "vector<" + vector_cs(n - 1) + ">"

    for var, d in vars.items():
        if d["type"] > 0:
            if d["dim"] >= 1:
                aargs += "move(" + var + "), "
            else:
                aargs += var + ", "
            fvar = var
            if var.lower() not in vars.keys():
                fvar = var.lower()
            fargs += vector_lint(d["dim"]) + " " + fvar + ", "
            input_part[0] += "\t" * indent
            input_part[0] += vector_lint(d["dim"]) + " " + var + ";\n"
        else:
            if "vertical_reducted" not in d:
                d["vertical_reducted"] = 0
            if d["dim"] + d["vertical_reducted"] >= 1:
                aargs += "move(" + var + "), "
            else:
                aargs += var + ", "
            fvar = var
            if var.lower() not in vars.keys():
                fvar = var.lower()
            fargs += (
                vector_cs(min(2, d["dim"] + d["vertical_reducted"])) + " " + fvar + ", "
            )
            input_part[0] += "\t" * indent
            input_part[0] += (
                vector_cs(min(2, d["dim"] + d["vertical_reducted"])) + " " + var + ";\n"
            )

    if len(aargs):
        aargs = aargs[:-2]
    if len(fargs):
        fargs = fargs[:-2]
    loopf = 0

    for ex_i in range(len(exs) - 1, -1, -1):
        indent = not ex_i
        ex = exs[ex_i]
        for es_i in range(len(ex)):
            es = ex[es_i]
            # print(es)
            if es[0]["class"] == "rep":
                loopf += 1
                size = convert_sub(es[0]["end"])
                for i in range(len(ex[es_i + 1])):
                    if ex[es_i + 1][i]["class"] != "query":
                        input_part[ex_i] += "\t" * indent
                        input_part[ex_i] += ex[es_i + 1][i]["name"]
                        for sub in ex[es_i + 1][i]["sub"]:
                            if sub != es[0]["loopvar"]:
                                input_part[ex_i] += "[" + sub + "]"
                        input_part[ex_i] += ".resize(" + size + ");\n"
                if ex[es_i + 1][0]["class"] == "query":
                    for var in query_vars:
                        input_part[ex_i] += "\t" * indent
                        input_part[ex_i] += var + ".resize(" + size + ");\n"
                        if len(ex[es_i + 1][0]["sub"]) == 0:
                            ex[es_i + 1][0]["sub"] = [es[0]["loopvar"]]

                input_part[ex_i] += "\t" * indent
                input_part[ex_i] += (
                    "rep("
                    + es[0]["loopvar"]
                    + ", "
                    + es[0]["begin"]
                    + ("" if es[0]["begin"] == "0" else "-1")
                    + ", "
                    + convert_sub(es[0]["end"])
                    + ("+1" if es[0]["begin"] == "0" else "")
                    + "){\n"
                )
                indent += 1
            elif es[0]["class"] == "query":
                input_part[ex_i] += "\t" * indent
                input_part[ex_i] += "in(q_type"
                for sub in es[0]["sub"]:
                    input_part[ex_i] += "[" + sub + "]"
                input_part[ex_i] += ");\n"
                for i in range(1, len(exs)):
                    input_part[ex_i] += "\t" * indent
                    input_part[ex_i] += (
                        "if(q_type["
                        + ex[es_i - 1][0]["loopvar"]
                        + "]=="
                        + exs[i][0][0]["num"]
                        + "){\n"
                    )
                    indent += 1
                    for line in input_part[i].split("\n")[:-1]:
                        input_part[ex_i] += "\t" * indent
                        input_part[ex_i] += line + "\n"
                    indent -= 1
                    input_part[ex_i] += "\t" * indent
                    input_part[ex_i] += "}\n"
            else:
                for i in range(len(es)):
                    if ex_i and input_type == "queries" and "name" in es[i]:
                        query_vars.add(es[i]["name"])
                    if es[i]["class"] == "var_vector":
                        input_part[ex_i] += "\t" * indent
                        input_part[ex_i] += es[i]["name"]
                        for sub in es[i]["sub"]:
                            input_part[ex_i] += "[" + sub + "]"
                        input_part[ex_i] += (
                            ".resize(" + convert_sub(es[i]["size"][0]) + ");\n"
                        )
                    if (
                        es[i]["class"] == "var_vector"
                        and es[i]["horizontal_offset"][0] != "1"
                    ):
                        input_part[ex_i] += "\t" * indent
                        input_part[ex_i] += (
                            "rep(_, "
                            + es[0]["horizontal_offset"][0]
                            + ", "
                            + convert_sub(es[i]["size"][0])
                            + ")in("
                            + es[i]["name"]
                        )
                        for sub in es[i]["sub"]:
                            input_part[ex_i] += "[" + sub + "]"
                        input_part[ex_i] += "[_]);\n"
                    elif (
                        es[i]["class"] == "var"
                        or es[i]["class"] == "var_charlist"
                        or es[i]["class"] == "var_vector"
                    ):
                        input_part[ex_i] += "\t" * indent
                        input_part[ex_i] += "in(" + es[i]["name"]
                        for sub in es[i]["sub"]:
                            input_part[ex_i] += "[" + sub + "]"
                        input_part[ex_i] += ");\n"
                if loopf:
                    loopf -= 1
                    indent -= 1
                    input_part[ex_i] += "\t" * indent
                    input_part[ex_i] += "}\n"

    if input_type == "testcases":
        input_part[0] += "\t" * indent
        input_part[0] += "while(" + exs[0][0][0]["name"] + "--){\n"
        indent += 1
        for line in input_part[1].split("\n")[:-1]:
            input_part[0] += "\t" * indent
            input_part[0] += line + "\n"
        input_part[0] += "\t" * indent
        input_part[0] += "solve(" + aargs + ");\n"
        indent -= 1
        input_part[0] += "\t" * indent
        input_part[0] += "}\n"
    else:
        input_part[0] += "\t" * indent
        input_part[0] += "solve(" + aargs + ");\n"

    # print(input_part[0])
    return success, aargs, fargs, input_part[0]
