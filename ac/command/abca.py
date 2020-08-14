# coding: utf-8

import os
import readline
from lark import Lark

class Transformer:
	def __default__(self, tree, env, d):
		print("unimplemented")
	
	def transform(self, tree, source, d):
		f = getattr(self, tree.data, self.__default__)
		return f(tree, source, d)

	def statement(self, tree, source, d):
		print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d+1)
		return

	def command(self, tree, source, d):
		print("  "*d,tree.data)
		f = getattr(self, tree.children[0].data, self.__default__)
		return f(source, tree.children[1:], d)

	def command_in(self, source, param, d):
		print("  "*d+"input")
		return

	def command_out(self, source, param, d):
		print("  "*d+"output")
		return

	def command_undo(self, source, param, d):
		print("  "*d+"undo")
		return

	def command_exit(self, source, param, d):
		print("  "*d+"exit")
		return -1

	def expr(self, tree, source, d):
		# print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d)
		return

	def expr1(self, tree, source, d):
		# print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d)
		return

	def expr2(self, tree, source, d):
		# print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d)
		return

	def expr3(self, tree, source, d):
		# print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d)
		return

	def expr4(self, tree, source, d):
		# print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d)
		return

	def expr5(self, tree, source, d):
		# print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d)
		return

	def expr6(self, tree, source, d):
		# print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d)
		return

	def expr7(self, tree, source, d):
		# print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d)
		return

	def expr8(self, tree, source, d):
		# print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d)
		return

	def expr9(self, tree, source, d):
		# print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d)
		return

	def expr10(self, tree, source, d):
		# print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d)
		return

	def expr11(self, tree, source, d):
		# print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d)
		return

	def expr12(self, tree, source, d):
		# print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d)
		return

	def expr13(self, tree, source, d):
		# print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d)
		return
	

	def decl(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def pluseq(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def minuseq(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def timeseq(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def diveq(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def poweq(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def modeq(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def lseq(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def rseq(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def _or(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def _xor(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def _and(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def _bor(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def _bxor(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def _band(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def eq(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def neq(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def lt(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def gt(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def leq(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def geq(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def ls(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def rs(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def plus(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def minus(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def times(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def div(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def mod(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def pow(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def test(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def value(self, tree, source, d):
		print("  "*d,tree.data)
		for e in tree.children:
			self.transform(e, source, d+1)
		return

	def number(self, tree, source, d):
		print("  "*d,tree.data)
		return

	def string(self, tree, source, d):
		print("  "*d,tree.data)
		return


def abca(args, config):
	rule = open('command/sub/abca_grammer.lark').read()
	parser = Lark(rule, start='statement', parser='lalr')
	source = ""
	while 1:
		statement = input(">> ")
		try:
			tree = parser.parse(statement)
		except:
			print("failed to parse")
			continue
		# print(tree.pretty())
		res = Transformer().transform(tree, source, 0)
		if res == -1:
			break
	return
