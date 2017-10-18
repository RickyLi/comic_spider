# !/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
from bs4 import BeautifulSoup

comic_url = u'http://comic.kukudm.com/comiclist/2049/'
save_file = u'./urls.txt'

def getUrls():
    content = urllib2.urlopen(comic_url)
    soup = BeautifulSoup(content,"lxml")

    links = soup.find_all('a')
    
    file_handler = open(save_file,'w')
    i = 0
    for item in links:
        link = item['href']
        if 'http://comic.kukudm.com/comiclist/' in link:
            file_handler.write( link+"\n" )
            i = i+1
            print('write into ' + save_file + ' ' + link)
    file_handler.close()

    print("Total write " + str(i) + " items into file.")


getUrls()
