# coding: utf-8

import os
import readline
from lark import Lark

class Transformer:
	def __default__(self, tree, env, d, data):
		print("unimplemented")
	
	def transform(self, tree, source, d, data):
		f = getattr(self, tree.data, self.__default__)
		return f(tree, source, d, data)

	def statement(self, tree, source, d, data):
		print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d+1, data)
		return

	def command(self, tree, source, d, data):
		print("  "*d,tree.data)
		f = getattr(self, tree.children[0].data, self.__default__)
		return f(source, tree.children[1:], d, data)

	def command_in(self, source, param, d, data):
		print("  "*d+"input")
		return

	def command_out(self, source, param, d, data):
		return self.transform(param[0], source, d+1, data)

	def command_undo(self, source, param, d, data):
		print("  "*d+"undo")
		return

	def command_exit(self, source, param, d, data):
		print("  "*d+"exit")
		exit(0)

	def expr(self, tree, source, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], source, d, data)

	def expr1(self, tree, source, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], source, d, data)

	def expr2(self, tree, source, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], source, d, data)

	def expr3(self, tree, source, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], source, d, data)

	def expr4(self, tree, source, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], source, d, data)

	def expr5(self, tree, source, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], source, d, data)

	def expr6(self, tree, source, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], source, d, data)

	def expr7(self, tree, source, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], source, d, data)

	def expr8(self, tree, source, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], source, d, data)

	def expr9(self, tree, source, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], source, d, data)

	def expr10(self, tree, source, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], source, d, data)

	def expr11(self, tree, source, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], source, d, data)

	def expr12(self, tree, source, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], source, d, data)

	def expr13(self, tree, source, d, data):
		# print("  "*d,tree.data)
		return self.transform(tree.children[0], source, d, data)

	
	def decl(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def tern(self, tree, source, d, data):
		print("  "*d,tree.data)
		l = self.transform(tree.children[0], source, d, data)
		m = self.transform(tree.children[1], source, d, data)
		r = self.transform(tree.children[2], source, d, data)
		print(l)
		return m if int(l) else r

	def pluseq(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def minuseq(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def timeseq(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def diveq(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def poweq(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def modeq(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def lseq(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def rseq(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def _or(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def _xor(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def _and(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def _bor(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def _bxor(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def _band(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def eq(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def neq(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def lt(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def gt(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def leq(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def geq(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def ls(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def rs(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def plus(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def minus(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def times(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def div(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def mod(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def pow(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def test(self, tree, source, d, data):
		print("  "*d,tree.data)
		return

	def value(self, tree, source, d, data):
		print("  "*d,tree.data)
		#for e in tree.children:
		return self.transform(tree.children[0], source, d+1, data)

	def number(self, tree, source, d, data):
		print("  "*d,tree.data)
		return tree.children[0].value

	def string(self, tree, source, d, data):
		print("  "*d,tree.data)
		return


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

		res = Transformer().transform(tree, source, 0, data)
		print(res)
	return
