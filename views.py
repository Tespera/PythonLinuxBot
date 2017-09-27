#coding:utf-8

from methord import docommand
import random

# def hello():
# 	content = '''
# 	/疑问/疑问/疑问/疑问/疑问/疑问/疑问
# 		咋滴啦？！干啥啊？
# 	/疑问/疑问/疑问/疑问/疑问/疑问/疑问
# 	'''
# 	return content
#
# def nihao():
# 	content = '''
# 		你好！你是谁？
# 		'''
# 	return content
#
# def sing():
# 	content = '''
# 		/白眼/白眼/白眼/白眼/白眼/白眼/白眼
# 			http://music.baidu.com/
# 			到这里去听啊，找我干啥！
# 		/白眼/白眼/白眼/白眼/白眼/白眼/白眼
# 		'''
# 	return content

def testPing():
	content = docommand('salt "*" test.ping')
	return content

