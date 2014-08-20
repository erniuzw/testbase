#-*-coding:GB2312-*-
import os
import base64
import sys
import datetime
try:
	import cPickle as pickle
except:
	import pickle

#预定义	
KEY = "9527"
tmpPath = "./tmp.txt"

#实现加密功能
class encryption(object):
	"""
	加密数字字符功能类
	"""

	def __init__(self, KEY):
		"""
		根据KEY初始化加密功能类
		"""
		self.strSequence = list("0123456789")
		self.strRandom = list(KEY)
		for item in self.strSequence:
			if item not in self.strRandom:
				self.strRandom.append(item)

		self.charSequence = list("abcdefghijklmnopqrstuvwxyz")
		self.charFragment = self.charSequence[int(KEY[0]):]

	def encrypt(self,num_):
		"""
		加密
		"""
		str_ = str(num_)
		tmp0 = []
		for item in str_:
			tmp0.append(self.strRandom[int(item)])
		tmp1 = []
		for item in tmp0:
			tmp1.append(self.charFragment[int(item)])
		temp = "".join(tmp1)
		temp = base64.encodestring(temp)
		return temp

	def decrypt(self, code_):
		"""
		解密
		"""
		temp = base64.decodestring(code_)
		tmp0 = []
		for item in temp:
			tmp0.append(self.charFragment.index(item))
		tmp1 = []
		for item in tmp0:
			tmp1.append(str(self.strRandom[item]))
		temp = "".join(tmp1)
		return int(temp)



def setInit():
	"""
	设置验证文件的辅助函数
	"""
	Encrypt = encryption(KEY)
	maxUSEnum = 15
	maxUSEnum = Encrypt.encrypt(maxUSEnum)
	lastUSEnum = 7
	lastUSEnum = Encrypt.encrypt(lastUSEnum)
	
	DICT = {}
	DICT['maxUSEnum'] = maxUSEnum
	DICT['lastUSEnum'] = lastUSEnum
	DICT['maxDatetime'] = datetime.datetime(2014,8,22,13,30,20)
	DICT['lastDatetime'] = datetime.datetime(2014,8,11,13,22,22)
	pickle.dump(DICT, open(tmpPath,"w"))

def count():
	DICT = pickle.load(open(tmpPath))
	Encrypt = encryption(KEY)
	
	maxUSEnum = DICT['maxUSEnum']
	maxUSEnum = Encrypt.decrypt(maxUSEnum)
	print u"最高使用次数为：%d" % maxUSEnum

	lastUSEnum = DICT['lastUSEnum']
	lastUSEnum = Encrypt.decrypt(lastUSEnum) + 1
	print u"当前使用次数为：%d" % lastUSEnum
	
	lastUSEnum1 = Encrypt.encrypt(lastUSEnum)
	DICT['lastUSEnum'] = lastUSEnum1
	pickle.dump(DICT, open(tmpPath,'w'))

	if lastUSEnum <= maxUSEnum:
		print u"还能正常使用"		
	else:
		print u"使用次数用尽"
		sys.exit()

def clock():
	DICT = pickle.load(open(tmpPath))
	maxDatetime = DICT['maxDatetime']
	lastDatetime = DICT['lastDatetime']
	today = datetime.datetime.today()
	print u"最后使用期限为：%s" % maxDatetime
	print u"上次使用时间为：%s" % lastDatetime
	print u"本次使用时间为：%s" % today
	

	if today <= lastDatetime:
		print u"系统日期错误"
		sys.exit()
	else:
		DICT['lastDatetime'] = today
		pickle.dump(DICT, open(tmpPath,"w"))

	if lastDatetime >= maxDatetime:
		print u"上次使用已过使用期限"
		sys.exit()	
	elif today >= maxDatetime:
		print u"本次使用已过使用期限"
		sys.exit()	
	else:
		print u"还能正常使用"

def test():
	print u"程序开始!"
	count()
	clock()
	print u"程序结束!"		
	
if __name__ == "__main__":
	setInit()
	test()


