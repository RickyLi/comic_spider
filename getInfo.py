#!/usr/bin/python
#-*- coding: UTF-8 -*-

import re,urllib2
from bs4 import BeautifulSoup
urls_path = u'./urls.txt'
info_path = u'./info.txt'


def getInfo():
	#fo = open(urls_path,'r')
	fw = open(info_path,'a+')

	with open(urls_path,'r') as fo:
		for line in fo:
			line = line.rstrip()
			soup = BeautifulSoup(urllib2.urlopen(line),'lxml')
			content = soup.find_all(text = re.compile(r'\W\S'))
			content = content[1:2][0]
			content = re.findall("\d+",content)
			
			content.insert(0,line[:len(line)-5])
			_content = ' '.join(content[:3])
			print(_content)
			fw.write(_content+"\n")

	fw.close()
	#fo.close()

getInfo()