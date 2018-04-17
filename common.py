# -*- coding: utf-8 -*-
import dbFunction

def getName(name):
    if(name.username == None):
        return name.first_name
    else:
        return '@'+name.username

def chechStatus(userID):
    status = False
    for users in dbFunction.getAllBlockedUsers():
        if(users[0] == str(userID)):
            status = True
    return status