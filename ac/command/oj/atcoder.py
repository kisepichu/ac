# coding: utf-8

import requests
import re
import urllib
import os
import sys
import lxml.html

class AtCoder:
	LOGIN_URL = 'https://atcoder.jp/login'

	def __init__(self):
		self.get_session()
		return

	def get_session(self):
		self.session = requests.Session()
		response = self.session.get(self.LOGIN_URL)
		tree = lxml.html.fromstring(response.text)
		self.csrf_token = tree.xpath('//*[@name="csrf_token"]/@value')[0]
		payload = {
			'username':os.environ.get('ac_id'),
			'password':os.environ.get('ac_password'),
			'csrf_token':self.csrf_token
		}
		self.session.post(self.LOGIN_URL, data=payload)
		return

	def get_problems(self, contest_id):
		res = self.session.get(f'https://atcoder.jp/contests/{contest_id}/submit')
		tree = lxml.html.fromstring(res.text)
		problem_ids = tree.xpath('//*[@id="select-task"]/option/@value')
		problems = []
		for problem_id in problem_ids:
			problems.append({'atcoder', contest_id, problem_id})
		return problems
	
	def download_testcases(self, problem):
		test_dir = f'data/testcase/atcoder/{problem[1]}/'
		if os.path.exists(test_dir):
			return -1
		os.makedirs(test_dir)

		res = self.session.get(f'https://atcoder.jp/contests/{problem[1]}/tasks/{problem[2]}?lang=ja')
		if res.status_code != 200:
			raise Exception(f'status_code {res.status_code}: https://atcoder.jp/contests/{problem[1]}/tasks/{problem[2]}?lang=ja')
		
		tree = lxml.html.fromstring(res.text)
		cnt = 0
		while len(tree.xpath(f'//h3[text()="入力例 {cnt+1}"]')):
			cnt += 1

			input_data = tree.xpath(f'//h3[text()="入力例 {cnt}"]')[0].getnext().text
			output_data = tree.xpath(f'//h3[text()="出力例 {cnt}"]')[0].getnext().text

			with open(test_dir + f'{problem[2]}_{cnt}.input', mode='w') as f:
				for line in input_data:
					f.write(line)
			with open(test_dir + f'{problem[2]}_{cnt}.output', mode='w') as f:
				for line in output_data:
					f.write(line)

		return cnt
	
	def submit(self, problem, language_id, source):
		payload = {
			'data.TaskScreenName':problem[2],
			'data.LanguageId':language_id,
			'sourceCode':source,
			'csrf_token':self.csrf_token
		}
		print(payload)
		return self.session.post(f'https://atcoder.jp/contests/{problem[1]}/submit', data=payload).content


