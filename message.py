#coding:utf-8

import qqbot
from run import response
from functools import partial
from setting import UserQQ,GroupQQ

@qqbot.QQBotSlot
def onQQMessage(bot,contact,member,content):
	'''
	上面注册的响应函数的函数名必须为 “onQQMessage” ，函数参数也必须和上面的一致
	:param bot: QQBot对象，即qq机器人
	:param contact: QContact 对象，消息的发送者，
					其 ctype 属性可以为 ‘buddy’/’group’/’discuss’ ，
					代表 好友/群/讨论组 对象，表示本消息是 好友消息/群消息/讨论组消息 。
	:param member: 仅当本消息为 群消息或讨论组消息 时有效，代表实际发消息的成员，
					它的 ctype 属性可以为 ‘group-member’/’discuss-member’ ，
					代表 群成员/讨论组成员 对象。当本消息为 好友消息 时， member 等于 None 。
	:param content: 内容
	'''
	if '@ME' in content:
		if contact.qq == GroupQQ:
			p = partial(response,bot,contact)
			p(content)

		# print(contact.qq)         #打印群号
		# print(member.qq)		  #打印@ME的QQ号
		# print(content)            #打印内容

if __name__ == '__main__':
	qqbot.RunBot(qq = UserQQ)