#-*-coding:GB2312-*-
import os
import base64
import sys
import datetime
try:
	import cPickle as pickle
except:
	import pickle

#Ԥ����	
KEY = "9527"
tmpPath = "./boot.db"

#ʵ�ּ��ܹ���
class encryption(object):
	"""
	���������ַ�������
	"""

	def __init__(self, KEY):
		"""
		����KEY��ʼ�����ܹ�����
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
		����
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
		����
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




def setInit():
	"""
	������֤�ļ��ĸ�������
	"""
	Encrypt = encryption(KEY)
	maxUSEnum = 150
	maxUSEnum = Encrypt.encrypt(maxUSEnum)
	lastUSEnum = 10
	lastUSEnum = Encrypt.encrypt(lastUSEnum)
	
	DICT = pickle.load(open(tmpPath))
	DICT['maxUSEnum'] = maxUSEnum
	DICT['lastUSEnum'] = lastUSEnum
	DICT['maxDatetime'] = datetime.datetime(2015,12,31,11,11,11)
	DICT['lastDatetime'] = datetime.datetime(2011,1,1,11,11,11)
	pickle.dump(DICT, open(tmpPath,"w"))

	
	
if __name__ == "__main__":
	setInit()


