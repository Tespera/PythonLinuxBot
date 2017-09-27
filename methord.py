#coding:utf-8

import re
import peewee
import paramiko
from setting import SSHCLIENT,DATABASE

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

def docommand(command):
	ssh_data = SSHCLIENT['defalut']
	ssh = paramiko.SSHClient()
	know_hosts = paramiko.AutoAddPolicy()
	ssh.set_missing_host_key_policy(know_hosts)

	ssh.connect(
		hostname = ssh_data['hostname'],
		port = ssh_data['port'],
		username = ssh_data['username'],
		password = ssh_data['password']
	)

	stdin,stdout,sdterr = ssh.exec_command(command)
	cont = stdout.read()
	ssh.close()
	return cont

def createDB():
	types = DATABASE['TYPE']
	if types == 'sqllite':
		db = peewee.SqliteDatabase(DATABASE['NAME'])
	else:
		db = None
	return db

class BaseModel(peewee.Model):
	class Meta:
		database = createDB()