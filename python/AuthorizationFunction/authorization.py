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


def count():
	"""
	��֤ʹ�ô���
	"""
	DICT = pickle.load(open(tmpPath))
	Encrypt01 = encryption(KEY)
	
	maxUSEnum = DICT['maxUSEnum']
	maxUSEnum = Encrypt01.decrypt(maxUSEnum)
	#print u"���ʹ�ô���Ϊ��%d" % maxUSEnum

	lastUSEnum = DICT['lastUSEnum']
	lastUSEnum = Encrypt01.decrypt(lastUSEnum) + 1
	#print u"��ǰʹ�ô���Ϊ��%d" % lastUSEnum
	
	lastUSEnum1 = Encrypt01.encrypt(lastUSEnum)
	DICT['lastUSEnum'] = lastUSEnum1
	pickle.dump(DICT, open(tmpPath,'w'))

	if lastUSEnum <= maxUSEnum:
		#print u"��������ʹ��"		
		return True
	else:
		#print u"ʹ�ô����þ�"
		#sys.exit()
		return False

def clock():
	"""
	��֤ʹ��ʱ��
	"""
	DICT = pickle.load(open(tmpPath))
	maxDatetime = DICT['maxDatetime']
	lastDatetime = DICT['lastDatetime']
	today = datetime.datetime.today()
	#print u"���ʹ������Ϊ��%s" % maxDatetime
	#print u"�ϴ�ʹ��ʱ��Ϊ��%s" % lastDatetime
	#print u"����ʹ��ʱ��Ϊ��%s" % today
	

	if today <= lastDatetime:
		#print u"ϵͳ���ڴ���"
		#sys.exit()
		return False
	else:
		DICT['lastDatetime'] = today
		pickle.dump(DICT, open(tmpPath,"w"))

	if lastDatetime >= maxDatetime:
		#print u"�ϴ�ʹ���ѹ�ʹ������"
		#sys.exit()
		return False
	elif today >= maxDatetime:
		#print u"����ʹ���ѹ�ʹ������"
		#sys.exit()
		return False
	else:
		#print u"��������ʹ��"
		return True

def authorization():
	#if clock() and count():
	if False and True:
		pass
	else:
		#print "��֤ʧ��"
		sys.exit()

	
if __name__ == "__main__":
	authorization()
	print "����ϵͳ"


