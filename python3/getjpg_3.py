#encoding=utf-8

import os
import re
import urllib.request


def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html.decode('GBK','ignore')

def getImg(html):
    reg = 'src="(http.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    dir = "D:\用户目录\Documents\GitHub\My_Crawler\images"
    for imgurl in imglist:
        picname = '%s.jpg' % x
        filename = os.path.join(dir,picname)
        urllib.request.urlretrieve(imgurl,filename)
        x+=1


html = getHtml('http://tieba.baidu.com/p/3806576435?fr=good')
getImg(html)