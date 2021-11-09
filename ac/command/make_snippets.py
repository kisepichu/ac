# coding: utf-8
import requests
import os
import sys
import shutil
import lxml.html
import glob
import subprocess


def make_snippet(config, filepath):
    path = filepath.split('/')
    categoly = path[-2]
    fil = path[-1]
    name = fil[:-4]
    title = name.replace('-', '_')
    title_no_underbar = name.replace('-', '')
    url = config['library_url'] + '/' + categoly + '/' + fil
    code = ''
    dependency = ''
    with open(fil, mode='r') as f:
        cont = f.readlines()
        for line in cont:
            if line == '#pragma once\n':
                continue
            elif line[:8] == '#include':
                dependency += '//.'+line.split('/')[-1].split('.')[0]+'\n'
            else:
                code += line

    session = requests.Session()
    res = session.get(url)
    tree = lxml.html.fromstring(res.text)
    x = tree.xpath(
        f'/html/body/div[@class=\'wrapper\']/section/ul[1]/li[2]')  # /ul/li
    version = x[0].text_content().split(':')[1][1:11]
    snippath = config['snippets_path'] + '/' + categoly + \
        f'/{title_no_underbar}Define.snippet'
    shutil.copyfile(os.path.dirname(os.path.abspath(__file__)) + '/../' +
                    config['template_snippet_path'], snippath)

    replacements = {
        '{% title %}': title,
        '{% title_no_underbar %}': title_no_underbar,
        '{% url %}': url,
        '{% version %}': version,
        '{% code %}': code,
        '{% dependency %}': dependency
    }
    out = []

    cont = []
    with open(snippath, mode='r', encoding='utf-8_sig') as f:
        cont = f.readlines()
        for i in range(len(cont)):
            for be, af in replacements.items():
                cont[i] = cont[i].replace(be, af)
    with open(snippath, mode='w') as f:
        for line in cont:
            f.write(line)


def make_snippets(args, config):
    os.chdir(config['library_path'])
    returncode = subprocess.call(['git', 'pull'])
    if returncode:
        print('pull failed')
        return 1
    os.chdir('./lib')
    folders = glob.glob('./*')
    for folder in folders:
        files = glob.glob(f'{folder}/*')
        categoly = folder.split('/')[-1]
        print(f'{categoly}')
        if not os.path.exists(categoly):
            os.mkdir(categoly)
        os.chdir(f'{folder}')
        for file in files:
            make_snippet(config, file)
            print('  ' + file.split('/')[-1])
        os.chdir('../')

    return
