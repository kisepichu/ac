# coding: utf-8

import os
import readline
from lark import Lark

class Transformer:
	def __default__(self, tree, env, d, data):
		print("unimplemented")
	
	def transform(self, tree, d, data):
		f = getattr(self, tree.data, self.__default__)
		return f(tree, d, data)

	def statement(self, tree, d, data):
		print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, d+1, data)
		return

	def command(self, tree, d, data):
		print("  "*d,tree.data)
		f = getattr(self, tree.children[0].data, self.__default__)
		return f(tree.children[1:], d, data)

	def command_in(self, param, d, data):
		print("  "*d+"input")
		return

	def command_out(self, param, d, data):
		return self.transform(param[0], d+1, data)

	def command_undo(self, param, d, data):
		print("  "*d+"undo")
		return

	def command_exit(self, param, d, data):
		print("  "*d+"exit")
		exit(0)

	def expr(self, tree, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], d, data)

	def expr1(self, tree, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], d, data)

	def expr2(self, tree, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], d, data)

	def expr3(self, tree, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], d, data)

	def expr4(self, tree, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], d, data)

	def expr5(self, tree, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], d, data)

	def expr6(self, tree, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], d, data)

	def expr7(self, tree, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], d, data)

	def expr8(self, tree, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], d, data)

	def expr9(self, tree, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], d, data)

	def expr10(self, tree, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], d, data)

	def expr11(self, tree, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], d, data)

	def expr12(self, tree, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], d, data)

	def expr13(self, tree, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], d, data)

	
	def decl(self, tree, d, data):
		print("  "*d,tree.data)
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
			else:
				print("unknown type: ", type(data[s]))
			source += " "+s+" = "+add
			return data[s], source

	def assign(self, tree, d, data):
		print("  "*d,tree.data)
		s = tree.children[0].children[0].value
		source = s+" = "
		r, add = self.transform(tree.children[1], d, data)
		source += add
		data[s] = r
		return data[s], source

	def tern(self, tree, d, data):
		print("  "*d,tree.data)
		l, add = self.transform(tree.children[0], d, data)
		source = add + " ? "
		m, add = self.transform(tree.children[1], d, data)
		source += add + " : "
		r, add = self.transform(tree.children[2], d, data)
		source += add
		return m if int(l) else r, source

	def pluseq(self, tree, d, data):
		print("  "*d,tree.data)
		s = tree.children[0].children[0].value
		source = s+" += "
		r, add = self.transform(tree.children[1], d, data)
		source += add
		data[s] += r
		return data[s], source

	def minuseq(self, tree, d, data):
		print("  "*d,tree.data)
		s = tree.children[0].children[0].value
		source = s+" -= "
		r, add = self.transform(tree.children[1], d, data)
		source += add
		data[s] -= r
		return data[s], source

	def timeseq(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def diveq(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def poweq(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def modeq(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def lseq(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def rseq(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def _or(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def _xor(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def _and(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def _bor(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def _bxor(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def _band(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def eq(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def neq(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def lt(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def gt(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def leq(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def geq(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def ls(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def rs(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def plus(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def minus(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def times(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def div(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def mod(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def pow(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def test(self, tree, d, data):
		print("  "*d,tree.data)
		return

	def value(self, tree, d, data):
		print("  "*d,tree.data)
		#for e in tree.children:
		return self.transform(tree.children[0], d+1, data)

	def number(self, tree, d, data):
		print("  "*d,tree.data)
		return int(tree.children[0].value), tree.children[0].value

	def string(self, tree, d, data):
		print("  "*d,tree.data)
		return tree.children[0].value[1:-1], tree.children[0].value
	
	def symbol(self, tree, d, data):
		print("  "*d,tree.data)
		s = tree.children[0].value
		if s in data:
			return data[s], s
		else:
			print("undefined")
			return 0, ""


def abca(args, config):
	rule = open('command/sub/abca_grammer.lark').read()
	parser = Lark(rule, start='statement', parser='lalr')
	source = ""
	data = {}
	while 1:
		statement = input(">> ")
		try:
			tree = parser.parse(statement)
		except:
			print("failed to parse")
			continue

		res, add = Transformer().transform(tree, 0, data)
		source += add+";\n"
		print("ret:",res)
		print("src:",source)
	return
