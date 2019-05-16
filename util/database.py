import sqlite3   # enable control of an sqlite database

def init(dbfile):
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, banned INTEGER);"
    c.execute(command)
    command = 'CREATE TABLE "pictures"(picId, picName, username, caption, private);'
    c.execute(command)
    db.commit()
    db.close()

#========================HELPER FXNS=======================

def table(tableName):
    '''
    PRINTS OUT ALL ROWS OF INPUT tableName
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT * FROM "{0}"'.format(tableName)
    c.execute(command)
    db.close()

#==========================================================
#Users table functions
def getUsers():
    '''
    RETURNS A DICTIONARY CONTAINING ALL CURRENT users AND CORRESPONDING PASSWORDS
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT username, password FROM USERS'
    c.execute(command)
    selectedVal = c.fetchall()
    db.close()
    return dict(selectedVal)

def findUser(username):
    '''
    CHECKS IF userName IS UNIQUE
    '''
    return username in getUsers()

def registerUser(userName, password):
    '''
    ADDS user TO USERS table. Upon registration, user inputs wanted currency
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    # userName is already in database -- do not continue to add
    if findUser(userName):
        db.close()
        return False
    # userName not in database -- continue to add
    else:
        command = 'INSERT INTO "users" VALUES(?, ?, ?)'
        c.execute(command, (userName, password, 0))
        db.commit()
        db.close()
        return True

def verifyUser(userName, password):
    '''
    CHECKS IF userName AND password MATCH THOSE FOUND IN DATABASE
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT username, password FROM USERS WHERE username = "{0}"'.format(userName)
    c.execute(command)
    selectedVal = c.fetchone()
    if selectedVal == None:
        db.close()
        return False
    if userName == selectedVal[0] and password == selectedVal[1]:
        db.close()
        return True
    db.close()
    return False
