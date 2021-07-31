# coding: utf-8

import os
import time
from datetime import datetime
from selenium import webdriver
<<<<<<< HEAD
from selenium.webdriver.chrome.options import Options
from command.oj.atcoder import AtCoder

class AtCoderProblems:
	devnull = open(os.devnull, 'w')
	atcoder = AtCoder()

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
		# self.session.get(f'https://kenkoooo.com/atcoder#/contest/show/{contest_id}')
		#time.sleep(3)
		cnt = 0
		problems = []
		while 1:
			try:
				elem = self.session.find_element_by_xpath(f"/html/body/div[@id='root']/div/div[@class='my-5 container']/div[@class='my-2'][1]/div[@class='row'][2]/div[@class='col']/div[@class='collapse show']/table[@class='table table-sm table-striped']/tbody/tr[{cnt + 1}]/td[1]/a")
				url = elem.get_attribute('href').split('/')
				problems.append(['atcoder',url[4],url[6]])
			except:
				#if not cnt:
				#	self.session.get(f'https://kenkoooo.com/atcoder#/contest/show/{contest_id}')
				#else:
				break
			cnt += 1
		print(problems)
		return problems

	def get_start_time(self, contest_id):
		self.session.get(f'https://kenkoooo.com/atcoder#/contest/show/{contest_id}')
		time.sleep(10)
		elem = self.session.find_element_by_xpath(f"/html/body/div[@id='root']/div/div[@class='my-5 container']/div[@class='my-2 row'][1]/div[@class='col-md-12 col-lg-6'][1]/table[@class='mb-0 table']/tbody/tr[1]/td")
		start_str = elem.text[:19]
		# print(start_str)
		# start_str = '2020-6-27 2:37:00+0900'
		return datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S')

	def get_contest_id(self, url):
		urlpath = url.fragment.split('/')
		if len(urlpath) >= 4 and urlpath[1] == 'contest':
			print(urlpath[3])
			return urlpath[3]
		else:
			return None
	def download_testcases(self, problem):
		return self.atcoder.download_testcases(problem)
	
	def submit(self, problem, language_id, source):
		return self.atcoder.submit(problem, language_id, source)
=======
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from command.oj.atcoder import AtCoder


class AtCoderProblems:
    devnull = open(os.devnull, 'w')
    atcoder = AtCoder()

    def __init__(self):
        self.get_session()
        return

    def get_session(self):
        option = Options()
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        option.binary_location = '/usr/bin/google-chrome'
        driver = webdriver.Chrome(ChromeDriverManager().install(), 0, option)
        self.session = driver
        return driver

    def get_problems(self, contest_id, f5=0):
        # self.session.get(f'https://kenkoooo.com/atcoder#/contest/show/{contest_id}')
        # time.sleep(3)
        cnt = 0
        problems = []
        while 1:
            try:
                elem = self.session.find_element_by_xpath(
                    f"/html/body/div[@id='root']/div/div[@class='my-5 container']/div[@class='my-2'][1]/div[@class='row'][2]/div[@class='col']/div[@class='collapse show']/table[@class='table table-sm table-striped']/tbody/tr[{cnt + 1}]/td[1]/a")
                url = elem.get_attribute('href').split('/')
                problems.append(['atcoder', url[4], url[6]])
            except:
                # if not cnt:
                #	self.session.get(f'https://kenkoooo.com/atcoder#/contest/show/{contest_id}')
                # else:
                break
            cnt += 1
        print(problems)
        return problems

    def get_start_time(self, contest_id):
        self.session.get(
            f'https://kenkoooo.com/atcoder#/contest/show/{contest_id}')
        time.sleep(10)
        elem = self.session.find_element_by_xpath(
            f"/html/body/div[@id='root']/div/div[@class='my-5 container']/div[@class='my-2 row'][1]/div[@class='col-md-12 col-lg-6'][1]/table[@class='mb-0 table']/tbody/tr[1]/td")
        start_str = elem.text[:19]
        # print(start_str)
        # start_str = '2020-6-27 2:37:00+0900'
        return datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S')

    def get_contest_id(self, url):
        urlpath = url.fragment.split('/')
        if len(urlpath) >= 4 and urlpath[1] == 'contest':
            print(urlpath[3])
            return urlpath[3]
        else:
            return None

    def download_testcases(self, problem):
        return self.atcoder.download_testcases(problem)

    def submit(self, problem, language_id, source):
        return self.atcoder.submit(problem, language_id, source)
>>>>>>> dev
