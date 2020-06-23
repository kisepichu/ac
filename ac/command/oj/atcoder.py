# coding: utf-8

import requests
import re
import urllib
import os
import sys
import lxml.html
import pathlib

class AtCoder:
	login_url = 'https://atcoder.jp/login'

	def __init__(self):
		self.get_session()
		return

	def get_session(self):
		self.session = requests.Session()
		response = self.session.get(self.login_url)
		tree = lxml.html.fromstring(response.text)
		self.csrf_token = tree.xpath('//*[@name="csrf_token"]/@value')[0]
		payload = {
			'username':os.environ.get('ac_id'),
			'password':os.environ.get('ac_password'),
			'csrf_token':self.csrf_token
		}
		self.session.post(self.login_url, data=payload)
		return

	def get_problems(self, contest_id):
		res = self.session.get(f'https://atcoder.jp/contests/{contest_id}/submit')
		tree = lxml.html.fromstring(res.text)
		problems = tree.xpath('//*[@id="select-task"]/option/@value')
		return problems
	
	def download_testcase(self):
		return

	def test(self):
		return
	
	def submit(self):
		return

	def dev(self,problem):
		print(self.get_problems(problem[1]))

