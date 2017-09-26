#coding:utf-8

from functools import partial
from urls import urlpatterns
from methord import takeRe

def response(request):
	p = partial(takeRe,request)
	for res,fun in urlpatterns:
		sendData = p(res,fun)
		if sendData:
			return sendData

#偏函数