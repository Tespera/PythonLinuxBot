#coding:utf-8

from functools import partial
from urls import urlpatterns
from methord import takeRe

def response(bot,contact,request):
	'''
	有人@ME，回答
	:param bot: 我
	:param contact: QQ群/组
	:param request: 是@ME请求的内容
	:return: 
	'''
	p = partial(takeRe,request)   #形成偏函数，将接收到的内容写入函数
	for res,fun in urlpatterns:
		sendData = p(res,fun)
		if sendData:
			bot.SendTo(contact,sendData)

#偏函数