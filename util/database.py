import sqlite3   # enable control of an sqlite database

def init():
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = "CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password TEXT, banned INTEGER);"
    c.execute(command)
    command = 'CREATE TABLE IF NOT EXISTS pictures (picId INTEGER PRIMARY KEY, picName TEXT, username TEXT, caption TEXT, private INTEGER);'
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
    command = 'SELECT username, password FROM USERS;'
    c.execute(command)
    selectedVal = c.fetchall()
    db.close()
    return dict(selectedVal)

def findUser(username):
    '''
    CHECKS IF username IS UNIQUE
    '''
    return username in getUsers()

def registerUser(username, password):
    '''
    ADDS user TO USERS table. Upon registration, user inputs wanted currency
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    # username is already in database -- do not continue to add
    if findUser(username):
        db.close()
        return False
    # username not in database -- continue to add
    else:
        command = 'INSERT INTO "users" VALUES(?, ?, ?);'
        c.execute(command, (username, password, 0))
        db.commit()
        db.close()
        return True

def verifyUser(username, password):
    '''
    CHECKS IF username AND password MATCH THOSE FOUND IN DATABASE
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT username, password FROM USERS WHERE username = "{0}";'.format(username)
    c.execute(command)
    selectedVal = c.fetchone()
    if selectedVal == None:
        db.close()
        return False
    if username == selectedVal[0] and password == selectedVal[1]:
        db.close()
        return True
    db.close()
    return False


#==========================================================
#Users table functions
def getPictures(username):
    '''
    RETURNS A array CONTAINING ALL CURRENT picture names for the user
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT picName FROM pictures WHERE username = "{0}";'.format(username)
    c.execute(command)
    selectedVal = c.fetchall()
    ans = [x[0] for x in selectedVal]
    db.close()
    return ans

def saveImage(username, picName, caption, private):
    '''
    ADDS picture TO pictures table
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    # username not in database -- continue to add
    if private == True:
        private = 1
    else:
        private = 0
    if picName in getPictures(username):
        db.close()
        return False
    command = 'INSERT INTO pictures VALUES(?, ?, ?, ?, ?);'
    c.execute(command, (None, picName, username, caption, private))
    db.commit()
    db.close()
    return True

def removeImage(username, picName):
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    if picName not in getPictures(username):
        db.close()
        return False
    command = 'DELETE FROM pictures WHERE username = ? AND picName = ?;'
    c.execute(command, (username, picName,))
    db.commit()
    db.close()
    return True
