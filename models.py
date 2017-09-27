#coding:utf-8

import peewee
from methord import BaseModel

class User(BaseModel):
	username = peewee.CharField(max_length = 32)
	password = peewee.CharField(max_length = 32)

if __name__ == '__main__':
	User.create_table()
