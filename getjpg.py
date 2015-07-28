__author__ = 'Administrator'

#coding = utf-8

import urllib
import re
import os

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r' src="(.+?\.jpg)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)

    dir = r'e:\github\My_Crawler\img'

    num = 0
    for imgurl in imglist:
        picname = '%s.jpg' % num
        filename = os.path.join(dir,picname)
        urllib.urlretrieve(imgurl, filename)

        num += 1

html = getHtml("http://tieba.baidu.com/p/3927014247")
getImg(html)