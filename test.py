#UTF-8

__author__ = 'Alvin'
import urllib.request
import os
import re

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
    response = urllib.request.urlopen(req)
    return response.read()

def get_page(url):
    html = url_open(url).decode('utf-8')
    pattern = r'<span class="current-comment-page">\[(\d{4})\]</span>' #������ʽѰ��ҳ���ַ

    page = int(re.findall(pattern,html)[0])
    return page



def find_imgs(page_url):
    pattern = r'<img src="(.*?\.jpg)"'
    html = url_open(page_url).decode('utf-8')
    img_addrs = re.findall(pattern,html)
    return img_addrs


def save_imgs(img_addrs,page_num,folder):
    os.mkdir(str(page_num))
    os.chdir(str(page_num))
    for i in img_addrs:
        pattern = r'sinaimg.cn/mw600/(.*?).jpg'
        filename = i.split('/')[-1]
        image = url_open(i)
        with open(filename,'wb') as f:
            f.write(image)
            f.close()


def download_mm(folder='ooxx',pages=10):
    os.mkdir(folder) #�½��ļ���
    os.chdir(folder) #��ת���ļ���
    folder_top = os.getcwd() #��ȡ��ǰ����Ŀ¼
    url = 'http://jandan.net/ooxx/'
    page_num = get_page(url) #��ȡ��ҳ���µĵ�ַ
    for i in range(pages):
        page_num -= i #�ݼ����ؼ�����ҳ
        page_url = url + 'page-' + str(page_num) + '#comments' #�����ҳ��ַ
        img_addrs = find_imgs(page_url) #��ȡͼƬ��ַ
        save_imgs(img_addrs,page_num,folder) #����ͼƬ
        os.chdir(folder_top)

if __name__ == '__main__':
    folder = input("Please enter a folder(default is 'ooxx'): " )
    pages = input("How many pages do you wan to download(default is 10): ")
    download_mm(str(folder),int(pages))