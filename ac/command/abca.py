# coding: utf-8

import os
import readline
import copy
import argparse
import pyperclip
from lark import Lark
from command.submit import submit

deb = 1
samplenum = 1
outputnum = 0
gdata = [{}]


def _command_in(names, inputs, outputs):
    global gdata
    global samplenum
    global outputnum
    source = ""
    for i in range(1, samplenum):
        gdata.append(copy.deepcopy(gdata[i-1]))
    for i in range(samplenum):
        for j in range(len(names)):
            if not i:
                source += "string " + \
                    names[j].upper()+"; cin >> "+names[j].upper()+";\n"
            try:
                gdata[i][names[j].lower()] = int(inputs[i][j])
                if deb >= 2:
                    print("int")
                if not i:
                    source += "lint " + \
                        names[j].lower()+" = stoll("+names[j].upper()+");\n"
            except:
                if deb >= 2:
                    print("string")
            gdata[i][names[j].upper()] = str(inputs[i][j])
        for j in range(len(outputs[i])):
            gdata[i]["out_"+str(j)] = str(outputs[i][j])

    return source


class Transformer:
    def __default__(self, tree, env, d, data):
        print("unimplemented")

    def transform(self, tree, d, data):
        f = getattr(self, tree.data, self.__default__)
        return f(tree, d, data)

    def statement(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        r, source = self.transform(tree.children[0], d+1, data)
        if len(tree.children) > 1:
            r, add = self.transform(tree.children[1], d, data)
        return r, source+';'

    def command(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        f = getattr(self, tree.children[0].data, self.__default__)
        return f(tree.children[1:], d, data)

    def command_in(self, param, d, data):
        print("  "*d+"input")
        global samplenum
        global outputnum
        print(samplenum)
        if samplenum != 1:
            return 0, ""
        names, _ = self.transform(param[0], d+1, data)
        inputs, _ = self.transform(param[1], d+1, data)
        outputs, _ = self.transform(param[2], d+1, data)
        samplenum = len(inputs)
        outputnum = len(outputs[0])
        return 0, _command_in(names, inputs, outputs)

    def command_out(self, param, d, data):
        print("  "*d+"output")
        print(samplenum)
        return self.transform(param[0], d+1, data)

    def command_undo(self, param, d, data):
        print("  "*d+"undo")
        return

    def command_exit(self, param, d, data):
        print("  "*d+"exit")
        exit(0)

    def illist(self, tree, d, data):
        print("  "*d+tree.data)
        ret = []
        for e in tree.children:
            r, _ = self.transform(e, d+1, data)
            ret.append(r)
        return ret, ""

    def ilist(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        ret = []
        for e in tree.children:
            r = e.children[0].children[0]
            ret.append(r)
        return ret, ""

    def expr(self, tree, d, data):
        # if deb>=3: print("  "*d+tree.data)
        return self.transform(tree.children[0], d, data)

    def expr1(self, tree, d, data):
        # if deb>=3: print("  "*d+tree.data)
        return self.transform(tree.children[0], d, data)

    def expr2(self, tree, d, data):
        # if deb>=3: print("  "*d+tree.data)
        return self.transform(tree.children[0], d, data)

    def expr3(self, tree, d, data):
        # if deb>=3: print("  "*d+tree.data)
        return self.transform(tree.children[0], d, data)

    def expr4(self, tree, d, data):
        # if deb>=3: print("  "*d+tree.data)
        return self.transform(tree.children[0], d, data)

    def expr5(self, tree, d, data):
        # if deb>=3: print("  "*d+tree.data)
        return self.transform(tree.children[0], d, data)

    def expr6(self, tree, d, data):
        # if deb>=3: print("  "*d+tree.data)
        return self.transform(tree.children[0], d, data)

    def expr7(self, tree, d, data):
        # if deb>=3: print("  "*d+tree.data)
        return self.transform(tree.children[0], d, data)

    def expr8(self, tree, d, data):
        # if deb>=3: print("  "*d+tree.data)
        return self.transform(tree.children[0], d, data)

    def expr9(self, tree, d, data):
        # if deb>=3: print("  "*d+tree.data)
        return self.transform(tree.children[0], d, data)

    def expr10(self, tree, d, data):
        # if deb>=3: print("  "*d+tree.data)
        return self.transform(tree.children[0], d, data)

    def expr11(self, tree, d, data):
        # if deb>=3: print("  "*d+tree.data)
        return self.transform(tree.children[0], d, data)

    def expr12(self, tree, d, data):
        # if deb>=3: print("  "*d+tree.data)
        return self.transform(tree.children[0], d, data)

    def expr13(self, tree, d, data):
        # if deb>=3: print("  "*d+tree.data)
        return self.transform(tree.children[0], d, data)

    def decl(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        s = tree.children[0].children[0].value
        if s in data:
            print("already defined")
            return data[s], ""
        else:
            data[s], add = self.transform(tree.children[1], d+1, data)
            source = ""
            if type(data[s]) == int:
                source = "lint"
            elif type(data[s]) == str:
                source = "string"
            elif type(data[s]) == list:
                source = "vector"
            else:
                print("unknown type: ", type(data[s]))
            source += " "+s+" = "+add
            return data[s], source

    def assign(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        s = tree.children[0].children[0].value
        source = s+" = "
        r, add = self.transform(tree.children[1], d, data)
        source += add
        if s not in data:
            print("undefined")
            return 0, ""
        data[s] = r
        return data[s], source

    def tern(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, add = self.transform(tree.children[0], d, data)
        source = add + " ? "
        m, add = self.transform(tree.children[1], d, data)
        source += add + " : "
        r, add = self.transform(tree.children[2], d, data)
        source += add
        return m if int(l) else r, source

    def pluseq(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        s = tree.children[0].children[0].value
        source = s+" += "
        r, add = self.transform(tree.children[1], d, data)
        source += add
        data[s] += r
        return data[s], source

    def minuseq(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        s = tree.children[0].children[0].value
        source = s+" -= "
        r, add = self.transform(tree.children[1], d, data)
        source += add
        data[s] -= r
        return data[s], source

    def timeseq(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        s = tree.children[0].children[0].value
        source = s+" *= "
        r, add = self.transform(tree.children[1], d, data)
        source += add
        data[s] *= r
        return data[s], source

    def diveq(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        s = tree.children[0].children[0].value
        source = s+" /= "
        r, add = self.transform(tree.children[1], d, data)
        source += add
        data[s] /= r
        return data[s], source

    def divveq(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        s = tree.children[0].children[0].value
        source = s+" /= "
        r, add = self.transform(tree.children[1], d, data)
        source += add
        data[s] //= r
        return data[s], source

    def poweq(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        s = tree.children[0].children[0].value
        source = s+" = pow("+s+", "
        r, add = self.transform(tree.children[1], d, data)
        source += add+")"
        data[s] **= r
        return data[s], source

    def modeq(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        s = tree.children[0].children[0].value
        source = s+" %= "
        r, add = self.transform(tree.children[1], d, data)
        source += add
        data[s] %= r
        return data[s], source

    def lseq(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        s = tree.children[0].children[0].value
        source = s+" <<= "
        r, add = self.transform(tree.children[1], d, data)
        source += add
        data[s] <<= r
        return data[s], source

    def rseq(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        s = tree.children[0].children[0].value
        source = s+" >>= "
        r, add = self.transform(tree.children[1], d, data)
        source += add
        data[s] >>= r
        return data[s], source

    def lor(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return (l or r), source+"||"+add

    def lxor(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return int((not not l) ^ (not not r)), "(!!("+source+"))^(!!("+add+"))"

    def land(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return (l and r), source+"&&"+add

    def bor(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return (l | r), source+"|"+add

    def bxor(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return (l ^ r), source+"^"+add

    def band(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return (l & r), source+"&"+add

    def eq(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return int(l == r), source+"=="+add

    def neq(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return int(l != r), source+"!="+add

    def lt(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return int(l < r), source+"<"+add

    def gt(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return int(l > r), source+">"+add

    def leq(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return int(l <= r), source+"<="+add

    def geq(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return int(l >= r), source+">="+add

    def ls(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return (l << r), source+"<<"+add

    def rs(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return (l >> r), source+">>"+add

    def plus(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return (l + r), source+"+"+add

    def minus(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return (l - r), source+"-"+add

    def times(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return (l * r), source+"*"+add

    def div(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return (l / r), source+"/"+add

    def divv(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return (l // r), source+"/"+add

    def mod(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return (l % r), source+"%"+add

    def pow(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        l, source = self.transform(tree.children[0], d, data)
        r, add = self.transform(tree.children[1], d, data)
        return (l ** r), "pow("+source+", "+add+")"

    def value(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        # for e in tree.children:
        return self.transform(tree.children[0], d+1, data)

    def number(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        return int(tree.children[0].value), tree.children[0].value

    def string(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        return tree.children[0].value[1:-1], tree.children[0].value

    def list(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        ret = []
        cnt = 0
        source = "{"
        for e in tree.children:
            r, add = self.transform(e, d, data)
            ret.append(r)
            if cnt:
                source += ", "
            source += add
            cnt += 1
        source += "}"
        return ret, source

    def choose(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        s = tree.children[0].children[0].value
        source = s
        r, add = self.transform(tree.children[1], d+1, data)
        source += "["+add+"]"
        if s not in data:
            print("undefined")
            return 0, ""
        return data[s][r], source

    def symbol(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        s = tree.children[0].value
        if s in data:
            return data[s], s
        else:
            print("undefined")
            return 0, ""

    def priority(self, tree, d, data):
        if deb >= 3:
            print("  "*d+tree.data)
        source = "("
        m, add = self.transform(tree.children[0], d+1, data)
        source += add+")"
        return m, source


def abca(args, config):
    rule = open('command/sub/abca_grammer.lark').read()
    parser = Lark(rule, start='statement', parser='lalr')
    source = ""
    global gdata
    global samplenum
    global outputnum
    samplenum = 1
    gdata = [{}]

    while 1:
        if args.input:
            print(pyperclip.paste())
            statement = pyperclip.paste()
            args.input = False
        else:
            statement = input(">> ")
        try:
            tree = parser.parse(statement)
        except:
            print("failed to parse")
            continue

        res = [0]*samplenum

        for i in range(samplenum):
            res[i], add = Transformer().transform(tree, 0, gdata[i])

        if add != "":
            source += add+"\n"

        if deb >= 2:
            print("source:", source, end='')
        if deb:
            print("return:", res)

        ac = 1
        ct = 0
        for i in range(len(res)):
            for j in range(outputnum):
                ct += 1
                r = res[i]
                if type(r) != list:
                    r = [r]
                print(ac)
                if j < len(r):
                    if str(r[j]) != gdata[i]["out_"+str(j)]:
                        ac = 0
                else:
                    ac = 0

        if not ct:
            ac = 0

        if ac == 1:
            source = source.split('\n')
            out = source[-2:][0]
            source = source[:-2]
            sub = ""
            for line in config['abca_header'].split('\\n'):
                sub += line + '\n'
            for line in source:
                sub += '	'+line+'\n'
            sub += '	cout << ('+out[:-1]+') << endl;\n'
            for line in config['abca_footer'].split('\\n'):
                sub += line + '\n'
            print(sub)
            with open(config['abca_path'], mode='w') as f:
                f.write(sub)
            option = argparse.Namespace()
            doption = {
                "force": 1,
                "source_path": config['abca_path'],
                "problem_char": "a",
                "no_format": 1
            }
            for e in doption.keys():
                vars(option)[e] = doption[e]
            submit(option, config)
            return
    return

# todo: 入力例をとる user script, 文字列/list アクセス, ラムダ式
# abca 以外にも対応するなら定数個でない入力数も
# 型が違うなど C++ のエラーをだす
