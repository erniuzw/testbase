#-*- coding:utf-8 -*-
import os
import sys
import datetime
import pickle
#验证程序

tmpPath = "./tmp.txt"

def setInit():
	DICT = {}
	DICT['maxUSEnum'] = 15
	DICT['lastUSEnum'] = 7
	DICT['maxDatetime'] = datetime.datetime(2014,8,22,13,30,20)
	DICT['lastDatetime'] = datetime.datetime(2014,8,21,13,22,22)
	pickle.dump(DICT, open(tmpPath,"w"))

def count():
	DICT = pickle.load(open(tmpPath))

	maxUSEnum = DICT['maxUSEnum']
	print u"最高使用次数为：%d" % maxUSEnum

	lastUSEnum = DICT['lastUSEnum'] + 1
	print u"当前使用次数为：%d" % lastUSEnum

	DICT['lastUSEnum'] = lastUSEnum
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
	os.system("cls")
	#setInit()
	test()
	#os.system("pause")