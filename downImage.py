#!/usr/bin/python
#-*- coding:UTF-8 -*-

import re,os,urllib2,requests
from bs4 import BeautifulSoup

info_path = u'./info.txt'
image_dir = u'./images/'
base_image_url = u'http://n.1whour.com/'

def downImage():
	with open(info_path,'r') as fo:
		for line in fo:
			line = line.rstrip().split(' ')
			print(line)
			base_url = line[0]
			dir_path = image_dir+line[1]
			page_num = int(line[2])+1

			#判断文件路径是否存在，不存在则创建文件目录
			if os.path.exists(dir_path):
				pass
			else:
				os.makedirs(dir_path)

			for i in range(1,page_num):
				_url = base_url + str(i) + '.htm'
				soup = BeautifulSoup(urllib2.urlopen(_url),'lxml')
				content = soup.find(text=re.compile(r'document.write'))
				content = re.findall("\+\"(.+?)'>", content)
				#content = re.findall(r"\+\"(.+?)'>", content)
				if len(content) > 0:
					image_url = base_image_url + content[0]
					arr = content[0].split('.')
					image_path = dir_path + '/' + str(i) + '.' + arr[len(arr)-1]
				
					r = requests.get(image_url)
					with open(image_path, "wb") as code:
						code.write(r.content)
					
					print(image_path)

downImage()