#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import urllib
import os
import re
import unittest

#filename = urllib.urlretrieve(url,'/Users/lihao/Downloads/%s'%'1.jpg')

def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
        @blocknum: 已经下载的数据块
        @blocksize: 数据块的大小
        @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%"% percent

class spider_pic:
	def __init__(self,url):
		self.url=url;
#url
	def get_req(self):
		user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		headers={'User-Agent':user_agent}
		req=urllib2.Request(self.url)
		return req
	def get_depage(self,req):
 		myresquest=urllib2.urlopen(req)
		mypage=myresquest.read()
		return mypage
	def get_page(self):
		req=self.get_req()
		page=self.get_depage(req)
		return page
	def get_ppage(self,page,res,flag=0):
		item=re.findall(res,page,re.L)
		item=set(item)
		if flag==1:
			with open('/Users/lihao/Downloads/tu/1','w') as wurl:
				for i in item:
					wurl.write(i+'\n')
		else:
			with open('/Users/lihao/Downloads/tu/url','a') as wurl:
				for i in item:
	                                wurl.write(i+'\n')
	def get_pic_url(self,res):
		 with open('/Users/lihao/Downloads/tu/1','r')as fi:
	                for url in fi:
                                t=url.rstrip('\n')
		 		b=spider_pic(t)
				req=b.get_req()
				page=b.get_depage(req)
				b.get_ppage(page,res)
				
	def get_pic(self):
		with open('/Users/lihao/Downloads/tu/url','r')as fi:
			for url in fi:
				t=url.rstrip('\n')
				filename=url.split('/')[-1]
				filename=filename.split('.')[0]
				try:
					if filename != 'IMG_2019':
						urllib.urlretrieve(url,'/Users/lihao/Downloads/tu/pic/%s.jpg'%filename,callbackfunc)
					print filename
				except:
					print 'error'
				
if __name__=="__main__":
	for i in range(3,10):
		with open('/Users/lihao/Downloads/tu/url','w') as gg:
			pass
		url='http://www.52moe.net/?paged=%s'%str(i)
		a=spider_pic(url)
#	urllib.urlretrieve(a.get_rep(),'/Users/lihao/Downloads/%s'%str(404))
		req=a.get_req()
		page=a.get_depage(req)
		a.get_ppage(page,'http://www\.52moe\.net/\?p=\d*',1)
		res='http://www\.52moe\.net/wp-content/uploads/\d{4,}/\d{2,}/IMG_.{3,10}\.jpg'
		a.get_pic_url(res)
		print (str(i)+'ok!')
		a.get_pic()

