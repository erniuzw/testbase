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
tmpPath = "./boot.db"

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
			tmp1.append(str(self.strRandom.index(str(item))))
		temp = "".join(tmp1)
		return int(temp)


def count():
	"""
	验证使用次数
	"""
	DICT = pickle.load(open(tmpPath))
	Encrypt01 = encryption(KEY)
	
	maxUSEnum = DICT['maxUSEnum']
	maxUSEnum = Encrypt01.decrypt(maxUSEnum)
	#print u"最高使用次数为：%d" % maxUSEnum

	lastUSEnum = DICT['lastUSEnum']
	lastUSEnum = Encrypt01.decrypt(lastUSEnum) + 1
	#print u"当前使用次数为：%d" % lastUSEnum
	
	lastUSEnum1 = Encrypt01.encrypt(lastUSEnum)
	DICT['lastUSEnum'] = lastUSEnum1
	pickle.dump(DICT, open(tmpPath,'w'))

	if lastUSEnum <= maxUSEnum:
		#print u"还能正常使用"		
		return True
	else:
		#print u"使用次数用尽"
		#sys.exit()
		return False

def clock():
	"""
	验证使用时间
	"""
	DICT = pickle.load(open(tmpPath))
	maxDatetime = DICT['maxDatetime']
	lastDatetime = DICT['lastDatetime']
	today = datetime.datetime.today()
	#print u"最后使用期限为：%s" % maxDatetime
	#print u"上次使用时间为：%s" % lastDatetime
	#print u"本次使用时间为：%s" % today
	

	if today <= lastDatetime:
		#print u"系统日期错误"
		#sys.exit()
		return False
	else:
		DICT['lastDatetime'] = today
		pickle.dump(DICT, open(tmpPath,"w"))

	if lastDatetime >= maxDatetime:
		#print u"上次使用已过使用期限"
		#sys.exit()
		return False
	elif today >= maxDatetime:
		#print u"本次使用已过使用期限"
		#sys.exit()
		return False
	else:
		#print u"还能正常使用"
		return True

def authorization():
	#if clock() and count():
	if False and True:
		pass
	else:
		#print "验证失败"
		sys.exit()

	
if __name__ == "__main__":
	authorization()
	print "进入系统"


