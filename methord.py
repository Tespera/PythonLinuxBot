#coding:utf-8

import re

def takeRe(content,res,function):
	'''
	当用户发送的内容匹配成功后，回复指定的内容
	:param content: 用户发送来的内容
	:param res: 用户urls当中定义的正则
	:param function: url匹配成功调用的函数
	:return: 
	'''
	result = re.search(res,content)
	if result:
		return function()
	else:
		return None