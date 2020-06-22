# -*- coding: utf-8 -*-

import requests
import re
import urllib
import os
import sys
import lxml.html
import pathlib

LOGIN_URL = 'https://atcoder.jp/login'

def get_session():
	s = requests.Session()
	r = s.get(LOGIN_URL)
	cookie = urllib.parse.unquote(r.headers['Set-Cookie'])
	pat = re.compile('csrf_token:.*=\x00')
	csrf_token = pat.search(cookie).group(0)[11:-1]
	payload = {
		'username': os.environ.get('ac_id'),
		'password': os.environ.get('ac_password'),
		'csrf_token': csrf_token
	}
	s.post(LOGIN_URL, data=payload)
	return s

def main():
	args = sys.argv
	session = get_session()
	print(f'https://atcoder.jp/contests/{args[1]}/tasks/{args[2]}?lang=ja')
	res = session.get(f'https://atcoder.jp/contests/{args[1]}/tasks/{args[2]}?lang=ja')
	tree = lxml.html.fromstring(res.text)
	cnt = 0
	pathlib.Path('./testcase').mkdir(exist_ok=True)

	while True:
		cnt += 1
		if len(tree.xpath(f'//h3[text()="入力例 {cnt}"]')) == 0:
			break
		input_data = tree.xpath(f'//h3[text()="入力例 {cnt}"]')[0].getnext().text
		output_data = tree.xpath(f'//h3[text()="出力例 {cnt}"]')[0].getnext().text

		path = pathlib.Path(f'./testcase/{args[2]}_in{cnt}.txt')
		path.touch()
		path.write_text(input_data.rstrip())

		path = pathlib.Path(f'./testcase/{args[2]}_out{cnt}.txt')
		path.touch()
		path.write_text(output_data.rstrip())

	print(f'Successfully downloaded {cnt} testcases')

if __name__ == '__main__':
	main()