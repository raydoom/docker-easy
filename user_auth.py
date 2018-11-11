# -*- coding: utf-8 -*-
__author__ = 'ma'


from user_config import USERS

def get_user_mapping():
    return dict([(user.username, user.password) for user in USERS])

user_mapping = get_user_mapping()

def user_auth(username, password):
	if user_mapping[username] == password:
		return True
	else:
		return False
