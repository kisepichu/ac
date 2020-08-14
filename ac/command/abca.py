# coding: utf-8

import os
import readline
from lark import Lark

class Transformer:
	def __default__(self, tree, env, d):
		print("unimplemented")
		exit(0)
	
	def transform(self, tree, source, d):
		f = getattr(self, tree.data, self.__default__)
		return f(tree, source, d)

	def statement(self, tree, source, d):
		print("  "*d+"statement(")
		for e in tree.children:
			self.transform(e, source, d+1)
		print("  "*d+")")
		return

	def command(self, tree, source, d):
		print("  "*d+"command")
		f = getattr(self, tree.children[0].data, self.__default__)
		return f(source, tree.children[1:], d)

	def command_in(self, source, param, d):
		print("  "*d+"input")
		return

	def command_out(self, source, param, d):
		print("  "*d+"output")
		return

	def command_exit(self, source, param, d):
		print("  "*d+"exit")
		return -1

	def value(self, tree, source, d):
		print("  "*d+"value(");
		for e in tree.children:
			self.transform(e, source, d+1)
		print("  "*d+")")
		return

	def number(self, tree, source, d):
		print("  "*d+"number("+tree.children[0].value+")");
		return

	def string(self, tree, source, d):
		print("  "*d+"string("+tree.children[0].value+")");
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
		res = Transformer().transform(tree, source, 0)
		if res == -1:
			break
	return
