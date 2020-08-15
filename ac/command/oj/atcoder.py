# coding: utf-8

import requests
import re
import urllib
import os
import sys
import lxml.html
import time
from datetime import datetime

class AtCoder:
	LOGIN_URL = 'https://atcoder.jp/login'

	def __init__(self):
		self.get_session()
		return

	def get_session(self):
		self.session = requests.Session()
		res = self.session.get(self.LOGIN_URL)
		tree = lxml.html.fromstring(res.text)
		self.csrf_token = tree.xpath('//*[@name="csrf_token"]/@value')[0]
		payload = {
			'username':os.environ.get('ac_id'),
			'password':os.environ.get('ac_password'),
			'csrf_token':self.csrf_token
		}
		self.session.post(self.LOGIN_URL, data=payload)
		return

	def get_statement_a(self, contest_id, f5=0):
		res = self.session.get(f'https://atcoder.jp/contests/{contest_id}/tasks_print?lang=ja')
		if f5:
			while res.status_code != 200:
				print(res.status_code)
				time.sleep(0.5)
				res = self.session.get(f'https://atcoder.jp/contests/{contest_id}/tasks_print?lang=ja')
		else:
			if res.status_code != 200:
				raise Exception(f'status_code {res.status_code}: https://atcoder.jp/contests/{contest_id}/tasks_print?lang=ja')
		
		tree = lxml.html.fromstring(res.text)
		statementx=tree.xpath(f'/html/body/div[@id="main-div"]/div[@id="main-container"]/div[@class="row"]/div[@class="col-sm-12"][1]/div[@id="task-statement"]/span[@class="lang"]/span[@class="lang-ja"]/div[@class="part"][1]/section')
		inputx=tree.xpath(f'/html/body/div[@id="main-div"]/div[@id="main-container"]/div[@class="row"]/div[@class="col-sm-12"][1]/div[@id="task-statement"]/span[@class="lang"]/span[@class="lang-ja"]/div[@class="io-style"]/div[@class="part"][1]/section')
		insamplex=tree.xpath(f'/html/body/div[@id=\'main-div\']/div[@id=\'main-container\']/div[@class=\'row\']/div[@class=\'col-sm-12\']/div[@id=\'task-statement\']/span[@class=\'lang\']/span[@class=\'lang-ja\']/div[@class=\'part\'][3]/section')
		outsamplex=tree.xpath(f'/html/body/div[@id=\'main-div\']/div[@id=\'main-container\']/div[@class=\'row\']/div[@class=\'col-sm-12\']/div[@id=\'task-statement\']/span[@class=\'lang\']/span[@class=\'lang-ja\']/div[@class=\'part\'][4]/section')
		
		statement=statementx[0].text_content()[5:]
		statement+="in.\n"+inputx[0][2].text_content()
		statement+="ex.\n"+insamplex[0][1].text_content()+"  ->  "+outsamplex[0][1].text_content()
		
		return statement


	def get_problems(self, contest_id, f5=0):
		res = self.session.get(f'https://atcoder.jp/contests/{contest_id}/submit')
		if f5:
			while res.status_code != 200:
				print(res.status_code)
				time.sleep(0.5)
				res = self.session.get(f'https://atcoder.jp/contests/{contest_id}/submit')
		else:
			if res.status_code != 200:
				raise Exception(f'status_code {res.status_code}: https://atcoder.jp/contests/{contest_id}/submit')
		
		tree = lxml.html.fromstring(res.text)
		problem_ids = tree.xpath('//*[@id="select-task"]/option/@value')
		problems = []
		for problem_id in problem_ids:
			problems.append(['atcoder', contest_id, problem_id])
		return problems

	def get_start_time(self, contest_id):
		res = self.session.get(f'https://atcoder.jp/contests/{contest_id}')
		tree = lxml.html.fromstring(res.text)
		start_str = tree.xpath('//*[@class="fixtime fixtime-full"]')[0].text_content()
		start_str = '2020-6-27 2:37:00+0900'
		return datetime.strptime(start_str[:-5], '%Y-%m-%d %H:%M:%S')

	def get_contest_id(self, urlpath):
		if len(urlpath) >= 2 and urlpath[0] == 'contests':
			return urlpath[1]
		else:
			return None
	
	def download_testcases(self, problem):
		test_dir = f'data/testcase/atcoder/{problem[1]}/'
		if os.path.exists(test_dir + f'{problem[2]}_1.input'):
			return -1
		if not os.path.exists(test_dir):
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
		# print(payload)
		return self.session.post(f'https://atcoder.jp/contests/{problem[1]}/submit', data=payload).content


