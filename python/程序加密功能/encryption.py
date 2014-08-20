#-*- coding:utf-8 -*-
import os
import base64
#加密数字字符
class verification(object):

	def __init__(self, KEY):
		self.strSequence = list("0123456789")
		self.strRandom = list(KEY)
		for item in self.strSequence:
			if item not in self.strRandom:
				self.strRandom.append(item)

		self.charSequence = list("abcdefghijklmnopqrstuvwxyz")
		self.charFragment = self.charSequence[int(KEY[0]):]

	def encrypt(self,str_):
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
		temp = base64.decodestring(code_)
		tmp0 = []
		for item in temp:
			tmp0.append(self.charFragment.index(item))
		tmp1 = []
		for item in tmp0:
			tmp1.append(str(self.strRandom[item]))
		return "".join(tmp1)

if __name__ == "__main__":
	KEY = "9527"
	test = verification(KEY)
	t1 = test.encrypt("15")
	t2 = test.decrypt("b2s=")
	print t1
	print t2
	os.system('pause')