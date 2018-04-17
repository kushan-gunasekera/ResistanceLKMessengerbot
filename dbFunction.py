# -*- coding: utf-8 -*-
import sqlite3
import configuration
import common

dbName = configuration.dbName

def connectDB():
    conn = sqlite3.connect(dbName, check_same_thread=False)
    c = conn.cursor()
    return conn, c

def addToAllUser(user):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("INSERT INTO allusers (userid, fname, lname, uname) VALUES ('"+ str(user.id) +"', '"+ str(user.first_name)+"', '"+ str(user.last_name) +"', '"+ str(user.username.lower()) +"')")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def updateToAllUser(user):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("UPDATE allusers SET fname='"+ str(user.first_name) +"', lname='"+ str(user.last_name) +"', uname='"+ str(user.username.lower()) +"' WHERE userid='"+ str(user.id) +"'")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def blockUser(user):
    status = False
    try:
        conn, c = connectDB()
        c.execute("INSERT INTO blockusers (userid) VALUES ('"+ str(user.id) +"')")
        conn.commit()
        status = True
    except Exception as e:
        status = False
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status

def getAllBlockedUsers():
    usersArray = []
    try:
        conn, c = connectDB()
        c.execute('SELECT b.userid, a.fname, a.lname, a.uname FROM blockusers b, allusers a WHERE a.userid=b.userid')
        for row in c.fetchall():
            usersArray.append(row)
    except Exception as e:
        usersArray = []
        raise e
    finally:
        c.close()
        conn.close()
        return usersArray

def unblockUser(userID):
    status = ''
    try:
        conn, c = connectDB()
        c.execute("DELETE FROM blockusers WHERE userid='"+ str(userID)+"'")
        conn.commit()
        status = 'success'
    except Exception as e:
        status = 'failed'
        conn.rollback()
        raise e
    finally:
        c.close()
        conn.close()
        return status