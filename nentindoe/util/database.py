import sqlite3   # enable control of an sqlite database

def init():
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = "CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password TEXT, banned INTEGER);"
    c.execute(command)
    command = 'CREATE TABLE IF NOT EXISTS pictures (picId INTEGER PRIMARY KEY, picName TEXT, username TEXT, caption TEXT, private INTEGER);'
    c.execute(command)
    command = 'CREATE TABLE IF NOT EXISTS allGroups (groupName TEXT UNIQUE);'
    c.execute(command)
    command = 'CREATE TABLE IF NOT EXISTS groupPics (picId INTEGER, groupName TEXT, banned INTEGER);'
    c.execute(command)
    command = 'CREATE TABLE IF NOT EXISTS groupMembership (username TEXT, groupName TEXT, admin INTEGER, request INTEGER, banned INTEGER);'
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
    #username does not exist
    if selectedVal == None:
        db.close()
        return False
    #correct
    if username == selectedVal[0] and password == selectedVal[1]:
        db.close()
        return True
    #username or password wrong
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

def getImage(username, picName):
    '''
    Returns a dictionary of the image file name as the key and the caption as the value
    '''
    #if the picName is not in use already
    if picName not in getPictures(username):
        return 0
    else:
        db = sqlite3.connect("data/draw.db")
        c = db.cursor()
        command = 'SELECT picId, caption FROM pictures WHERE username = ? AND picName = ?;'
        c.execute(command,(username,picName,))
        selectedVal = c.fetchall()
        print(selectedVal)
        ans = {}
        for x in selectedVal:
            ans[picName + "_" + str(x[0]) + ".png"] = x[1]
        db.close()
        return ans

def getImageId(username, picName):
    '''
    retuns the image id of a specified image or 0 if it dont exist
    '''
    if picName not in getPictures(username):
        return 0
    else:
        db = sqlite3.connect("data/draw.db")
        c = db.cursor()
        command = 'SELECT picId FROM pictures WHERE username = ? AND picName = ?;'
        c.execute(command,(username,picName,))
        selectedVal = c.fetchall()
        db.close()
        return selectedVal[0][0]

def saveImage(username, picName, caption, private):
    '''
    ADDS picture TO pictures table, returns the image id
    '''
    if username not in getUsers():
        return -1
    if picName in getPictures(username):
        return 0
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    # username not in database -- continue to add
    if private == True:
        private = 1
    else:
        private = 0
    command = 'INSERT INTO pictures VALUES(?, ?, ?, ?, ?);'
    c.execute(command, (None, picName, username, caption, private))
    db.commit()
    db.close()
    return getImageId(username, picName)

def removeImage(username, picName):
    '''
    removes an image from the db
    '''
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

#==========================================================
#creating group functions

def getGroups():
    '''
    RETURNS A DICTIONARY CONTAINING ALL CURRENT users AND CORRESPONDING PASSWORDS
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT * FROM allGroups;'
    c.execute(command)
    selectedVal = c.fetchall()
    ans = [x[0] for x in selectedVal]
    db.close()
    return ans

def findGroup(groupName):
    '''
    CHECKS IF username IS UNIQUE
    '''
    return groupName in getGroups()

def createGroup(username, groupName):
    '''
    ADDS user TO USERS table. Upon registration, user inputs wanted currency
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    # username is already in database -- do not continue to add
    if findGroup(groupName):
        db.close()
        return False
    # username not in database -- continue to add
    else:
        command = 'INSERT INTO "allGroups" VALUES(?);'
        c.execute(command, (username,))
        command = 'INSERT INTO "groupMembership" VALUES(?,?,?,?,?);'
        c.execute(command, (username,groupName,1,0,0))
        db.commit()
        db.close()
        return True

#==========================================================
#requesting group functions
def getRequests(username):
    '''
    RETURNS A DICTIONARY CONTAINING ALL CURRENT users AND CORRESPONDING PASSWORDS
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT groupName FROM groupMembership WHERE username = (?);'
    c.execute(command,(username,))
    selectedVal = c.fetchall()
    ans = [x[0] for x in selectedVal]
    db.close()
    return ans

def groupInRequests(username, groupName):
    '''
    CHECKS IF username IS UNIQUE
    '''
    return groupName in getRequests(username)

def requestGroup(username, groupName):
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    # username is already in database -- do not continue to add
    if groupInRequests(groupName):
        db.close()
        return False
    # username not in d
    else:
        command = 'INSERT INTO "groupMembership" VALUES(?,?,?,?,?);'
        c.execute(command, (username,groupName,0,1,0))
        db.commit()
        db.close()
        return True
#==========================================================
#accepting requesting functions
def acceptRequest():
    pass
