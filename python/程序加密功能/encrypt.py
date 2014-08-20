#-*- coding:utf-8 -*-
import base64

KEY = "9527"
#base64.encodestring()
#base64.decodestring()

strSequence = list("0123456789")
strRandom = list(KEY)
for item in strSequence:
	if item not in strRandom:
		strRandom.append(item)

charSequence = list("abcdefghijklmnopqrstuvwxyz")
charFragment = charSequence[int(KEY[0]):]

def encrypt(str_):
	tmp0 = []
	for item in str0:
		tmp0.append(strRandom[int(item)])
	tmp1 = []
	for item in tmp0:
		tmp1.append(charFragment[int(item)])
	return "".join(tmp1)

def decrypt(code_):
	tmp0 = []
	for item in code_:
		tmp0.append(charFragment.index(item))
	tmp1 = []
	for item in tmp0:
		tmp1.append(str(strRandom[item]))
	return "".join(tmp1)


print encrypt(str0)
print decrypt("ok")