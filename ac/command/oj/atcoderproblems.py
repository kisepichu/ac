# coding: utf-8

import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class AtCoderProblems:
	devnull = open(os.devnull, 'w')

	def __init__(self):
		self.get_session()
		return

	def get_session(self):
		option = Options()
		option.add_argument('--headless')
		option.add_argument('--no-sandbox')
		option.binary_location = '/usr/bin/google-chrome'
		driver = webdriver.Chrome('/usr/local/bin/chromedriver', 0, option)
		self.session = driver
		return driver

	def get_problems(self, contest_id, f5=0):
		
		return

	def get_start_time(self, contest_id):
		res = self.session.get(f'https://kenkoooo.com/atcoder#/contest/show/{contest_id}')
		time.sleep(2)
		with open('test.txt',mode='w') as f: f.write(self.session.page_source)
		elem = self.session.find_element_by_xpath(f"/html/body/div[@id='root']/div/div[@class='my-5 container']/div[@class='my-2 row'][1]/div[@class='col-md-12 col-lg-6'][1]/table[@class='mb-0 table']/tbody/tr[1]/td")
		start_str = elem.text[:19]
		# print(start_str)
		# start_str = '2020-6-27 2:37:00+0900'
		return datetime.datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S')

	def get_contest_id(self, url):
		urlpath = url.fragment.split('/')
		if len(urlpath) >= 4 and urlpath[1] == 'contest':
			print(urlpath[3])
			return urlpath[3]
		else:
			return None