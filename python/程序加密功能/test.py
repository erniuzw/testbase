#-*- coding:utf-8 -*-
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
		return "".join(tmp1)

	def decrypt(self, code_):
		tmp0 = []
		for item in code_:
			tmp0.append(self.charFragment.index(item))
		tmp1 = []
		for item in tmp0:
			tmp1.append(str(self.strRandom[item]))
		return "".join(tmp1)

if __name__ == "__main__":
	KEY = "9527"
	test = verification(KEY)
	print test.encrypt("0123456789")
	print test.decrypt("ok")
	test0 = verification("85423")
	print test0.encrypt("15")