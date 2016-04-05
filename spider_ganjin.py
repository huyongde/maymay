#coding=utf-8

import urllib, httplib
from bs4 import BeautifulSoup
import sys, datetime
import os
import time

##
# 通过详情页获得所有大图的列表
# @param href_link 详情页url
# @return list 大图的url列表
###
def get_big_image_urls(href_link):
    content = urllib.urlopen(href_link).read()
    soup = BeautifulSoup(content)
    big_image_url_list = []
    for link in soup.find_all("a"):
        if (link.get("title")) == u"查看大图":
            big_image_url_list.append(link.img.get("src"))
    return big_image_url_list 

###
# 保存src对应的图片到磁盘
# @param src image的url
# @param save_path 图片存储的路径
# @return none
###
def save_big_image(src, save_path):
    tmp_list = src.split("/")
    image_name = tmp_list[-1]
    content = urllib.urlopen(src).read()
    fh = open(save_path + "/" + image_name, "wb")
    fh.write(content)
    fh.close()


conn = httplib.HTTPConnection("bj.ganji.com", 80)
headers = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
    "referer" : "bj.ganji.com",
}
conn.request("GET", "/dahang/", '', headers) 
res = conn.getresponse()
#print res.status
#print res.reason
#print res.getheaders()
body = res.read()
soup = BeautifulSoup(body)

today = time.strftime("%Y%m%d", time.localtime())
save_path = "ganji-images/" + today
if os.path.exists(save_path) == False:
    os.mkdir(save_path)
else:
    print save_path + " exists, please check"

for link in soup.find_all("a"):
    if (link.img):
        img_url = link.img.get("data-original")
        if img_url:
            #print link
            href_link = link.get("href")
            image_url_list = get_big_image_urls(href_link)
            for src in image_url_list:
                print src
                save_big_image(src, save_path)

