#!/usr/bin/env python
#-*- coding: utf-8 -*-


import urllib2
import urllib
import unittest
import os

class download_dome:
		'''初始化
		   @url: 下载目标地址
		   @path: 文件存储路径
		   @ftype: 文件类型
		'''
	def __init__(self,url,path,ftype):
		'''初始化
		   @url: 下载目标地址
		   @path: 文件存储路径
		   @ftype: 文件类型
		'''
		self.url=url
		self.path=path
		self.ftype=ftype
	def callbackfunc(self,blocknum,blocksize,totalsize):
		'''回调函数
		   @blockknum: 已经下载的数据块
		   @blocksize: 数据块的大小
		   @totalsize: 远程文件的大小
		'''
		percent= 100.0*blocknum*blocksize/totalsize
		if percent>100:
		   percent=100
		if percent>=100:
		   print self.filename,
		print "%.2f%%"% percent

	def download_url(self):
		'''
			根据url下载文件
			url的最后/后面的为文件名
		'''
		t=self.url.rstrip('\n').rstrip('\r')
		filename=t.split('/')[-1]
		filename=filename.split('.')[0]
		self.filename=filename
		try:
		 	os.path.exists(self.path)
		except:
			os.mkdir(self.path)
		try:
			fp=self.path+filename+self.ftype
			urllib.urlretrieve(t,fp,self.callbackfunc)
		except:
			print (filename+' error')
	
		
if __name__=="__main__":
	url=raw_input('')
	path=raw_input('')
	ftype=raw_input('')
	a=download_dome(url,path,ftype)
	a.download_url()
