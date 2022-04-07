# coding: utf-8


def format(s):
    summary = []
    full = []
    s = s.split("\n")

    output_flag = 0
    sta = ["root"]
    summary += ["#ifdef SUMMARY // I †obfuscate† the code so that it won't be read"]
    for i in range(len(s)):
        line = s[i]
        if line.startswith("#pragma region") or line.startswith("#pragma endregion"):
            line = "//" + line
        if line == "//sub-BOF":
            output_flag = 1
        if line.startswith("//#pragma region"):
            tmp = line.split()
            sta.append(tmp[2])
        if output_flag:
            full += [line]
        if line.startswith("//#pragma region lib_"):
            tmp = "#library <" + sta[-1][4:] + ">"
            # tmp = '+library{ name:' + sta[-1][4:]
            # if s[i+1].startswith('//,'):
            #     tmp += s[i+1][2:]
            # tmp += ' }'
            summary += [tmp]
        if sta[-1] == "solve" and not line.startswith("//#"):
            summary += [line]
        if line.startswith("//#pragma endregion"):
            sta.pop()
        if line == "//sub-EOF":
            output_flag = 0
    summary += ["#endif // SUMMARY", ""]

    return "\n".join(summary + full)
