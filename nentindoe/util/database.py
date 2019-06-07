import sqlite3   # enable control of an sqlite database

def init():
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = "CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password TEXT, banned INTEGER);"
    c.execute(command)
    command = 'CREATE TABLE IF NOT EXISTS pictures (picId TEXT, picName TEXT, username TEXT, caption TEXT);'
    c.execute(command)
    command = 'CREATE TABLE IF NOT EXISTS allGroups (groupName TEXT UNIQUE);'
    c.execute(command)
    command = 'CREATE TABLE IF NOT EXISTS groupPics (picId TEXT, groupName TEXT, banned INTEGER);'
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

def registerUser(username):
    '''
    ADDS user TO USERS table
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    # username is already in database -- do not continue to add
    if findUser(username):
        db.close()
        return False
    # username not in database -- continue to add
    else:
        command = 'INSERT INTO "users" VALUES (?, ?, ?);'
        c.execute(command, (username, "hello", 0))
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
    RETURNS A array CONTAINING ALL CURRENT picture ids for the user
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT picId FROM pictures WHERE username = "{0}";'.format(username)
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
    else: #only if the picName in use
        db = sqlite3.connect("data/draw.db")
        c = db.cursor()
        command = 'SELECT picId FROM pictures WHERE username = ? AND picName = ?;'
        c.execute(command,(username,picName,))
        selectedVal = c.fetchall()
        db.close()
        return selectedVal[0][0]

def saveImage(picid,username):
    '''
    ADDS picture TO pictures table, returns the image id
    '''
    if username not in getUsers(): #the user does not exist
        return -1
    # if picName in getPictures(username): #the picture already exists
    #     return 0
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    # username not in database -- continue to add
    # if private == True:
    #     private = 1
    # else:
    #     private = 0
    command = 'INSERT INTO pictures VALUES(?, ?, ?, ?);'
    print(picid)
    print(username)
    c.execute(command, (picid, 'tset', username, 'test'))
    db.commit()
    db.close()
    return  #returns the pic id

def removeImage(username, picName):
    '''
    removes an image from the db
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    if picName not in getPictures(username): #if the pic does not exist
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
    RETURNS A LIST CONTAINING ALL CURRENT groups
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
    CHECKS IF groupName IS UNIQUE
    '''
    return groupName in getGroups()

def createGroup(username, groupName):
    '''
    ADDS group TO allGroups TABLE. ADDS A LISTING TO THE groupMembership TABLE
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
        c.execute(command, (groupName,))
        command = 'INSERT INTO "groupMembership" VALUES (?,?,?,?,?);'
        c.execute(command, (username,groupName,1,0,0))
        db.commit()
        db.close()
        return True

#==========================================================
#requesting group functions
def getJoined(username):
    '''
    RETURNS A LIST CONTAINING ALL joined groups FOR A user
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT groupName FROM groupMembership WHERE username = (?) and request = 0;'
    c.execute(command,(username,))
    selectedVal = c.fetchall()
    ans = [x[0] for x in selectedVal]
    db.close()
    return ans

def getPending(username):
    '''
    RETURNS A LIST CONTAINING ALL pending groups FOR A user
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT groupName FROM groupMembership WHERE username = (?) and request = 1;'
    c.execute(command,(username,))
    selectedVal = c.fetchall()
    ans = [x[0] for x in selectedVal]
    db.close()
    return ans

def groupInPending(username, groupName):
    '''
    CHECKS IF the group is in the users pending groups
    '''
    return groupName in getPending(username)

def groupInJoined(username, groupName):
    '''
    CHECKS IF the group is in the users joined groups
    '''
    return groupName in getJoined(username)

def requestGroup(username, groupName):
    '''
    Send a request to a group from the current user
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    if groupInPending(username,groupName) or groupInJoined(username, groupName): # user does not have a request active on this group or is already in it
        db.close()
        return False
    else:
        command = 'INSERT INTO "groupMembership" VALUES (?,?,?,?,?);'
        c.execute(command, (username,groupName,0,1,0))
        db.commit()
        db.close()
        return True

#==========================================================
#accepting requesting functions
def getAdminGroups(username):
    '''
    RETURNS A LIST CONTAINING ALL groups where the user is an admin
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT groupName FROM groupMembership WHERE username = (?) AND admin = 1;'
    c.execute(command,(username,))
    selectedVal = c.fetchall()
    ans = [x[0] for x in selectedVal]
    db.close()
    return ans

def getRequests(username):
    '''
    RETURNS A DICTIONARY OF ALL the groups, that the User is an admin in, as keys
    and a list of the users that requested to join those groups as the values
    '''
    adminGroups = getAdminGroups(username)
    val = {}
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    for groupName in adminGroups:
        command = 'SELECT username FROM groupMembership WHERE groupName = (?) AND request = 1;'
        c.execute(command,(groupName,))
        selectedVal = c.fetchall()
        ans = [x[0] for x in selectedVal]
        val[groupName] = ans
    db.close()
    return val

def evalRequest(groupName, admin, member, value):
    '''
    If value is 1 then accepts the request, if value is 0 then it denys the request
    '''
    requests = getRequests(admin)
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    if groupName not in requests.keys():
        return False
    if member not in requests[groupName]:
        return False

    if value == 1:
        command = 'UPDATE groupMembership SET request = 0 WHERE groupName = (?) AND username = (?);'
        c.execute(command,(groupName, member))
        db.commit()
        db.close()
        return True
    elif value == 0:
        command = 'DELETE FROM groupMembership WHERE groupName = (?) AND username = (?);'
        c.execute(command,(groupName, member))
        db.commit()
        db.close()
        return True
    return False

#==========================================================
#group administration functions
def getMembers(groupName):
    '''
    RETURNS A LIST of all members given a groupName
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT username FROM groupMembership WHERE groupName = (?) AND admin = 0 AND request = 0 AND banned = 0;'
    c.execute(command,(groupName,))
    selectedVal = c.fetchall()
    ans = [x[0] for x in selectedVal]
    db.close()
    return ans

def getAdmins(groupName):
    '''
    RETURNS A LIST of all admins given a groupName
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT username FROM groupMembership WHERE groupName = (?) AND admin = 1 AND request = 0 AND banned = 0;'
    c.execute(command,(groupName,))
    selectedVal = c.fetchall()
    ans = [x[0] for x in selectedVal]
    db.close()
    return ans

def getBanned(groupName):
    '''
    RETURNS A LIST of all banned members given a groupName
    '''
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT username FROM groupMembership WHERE groupName = (?) AND request = 0 AND banned = 1;'
    c.execute(command,(groupName,))
    selectedVal = c.fetchall()
    ans = [x[0] for x in selectedVal]
    db.close()
    return ans

def banMember(groupName, member):
    '''
    Bans a member only if the member is alredy in the group and not an Admin
    '''
    if member not in getMembers(groupName):
        return False
    else:
        db = sqlite3.connect("data/draw.db")
        c = db.cursor()
        command = 'UPDATE groupMembership SET banned = 1 WHERE groupName = (?) AND username = (?);'
        c.execute(command,(groupName, member))
        db.commit()
        db.close()
        return True

def unbanMember(groupName, member):
    '''
    unBans a member only if the member is alredy in the group and already banned
    '''
    if member not in getBanned(groupName):
        return False
    else:
        db = sqlite3.connect("data/draw.db")
        c = db.cursor()
        command = 'UPDATE groupMembership SET banned = 0 WHERE groupName = (?) AND username = (?);'
        c.execute(command,(groupName, member))
        db.commit()
        db.close()
        return True

def kickMember(groupName, member):
    '''
    Kicks a member or admin only if the member is alredy in the group
    '''
    if member not in getMembers(groupName) and member not in getAdmins(groupName):
        return False
    else:
        db = sqlite3.connect("data/draw.db")
        c = db.cursor()
        command = 'DELETE FROM groupMembership WHERE groupName = (?) AND username = (?);'
        c.execute(command,(groupName, member))
        db.commit()
        db.close()
        return True

def promoteMember(groupName, member):
    '''
    Promotes a member only if the member is alredy in the group and not an admin
    '''
    if member not in getMembers(groupName):
        return False
    else:
        db = sqlite3.connect("data/draw.db")
        c = db.cursor()
        command = 'UPDATE groupMembership SET admin = 1 WHERE groupName = (?) AND username = (?);'
        c.execute(command,(groupName, member))
        db.commit()
        db.close()
        return True

def demoteMember(groupName, member):
    '''
    demotes an admin
    '''
    if member not in getAdmins(groupName):
        return False
    else:
        db = sqlite3.connect("data/draw.db")
        c = db.cursor()
        command = 'UPDATE groupMembership SET admin = 0 WHERE groupName = (?) AND username = (?);'
        c.execute(command,(groupName, member))
        db.commit()
        db.close()
        return True

def addMember(groupName, member):
    '''
    admin adds a member
    '''
    if member not in getAdmins(groupName) and member not in getMembers() and member not in getBanned():
        return False
    else:
        requestGroup(member, groupName)
        db = sqlite3.connect("data/draw.db")
        c = db.cursor()
        command = 'UPDATE groupMembership SET request = 0 WHERE groupName = (?) AND username = (?);'
        c.execute(command,(groupName, member))
        db.commit()
        db.close()
        return True


def deleteGroup(groupName):
    '''
    Deletes a group.
    '''
    if group not in getGroups():#if the group does not exist
        return False
    else:
        db = sqlite3.connect("data/draw.db")
        c = db.cursor()
        command = 'DELETE FROM groupMembership WHERE groupName = (?);'
        c.execute(command,(groupName))
        command = 'DELETE FROM allGroups WHERE groupName = (?);'
        c.execute(command,(groupName))
        db.commit()
        db.close()
        return True

#==========================================================
#group imaging functions
def getGroupPicIds(groupName):
    db = sqlite3.connect("data/draw.db")
    c = db.cursor()
    command = 'SELECT picId FROM groupPics WHERE groupName = (?);'
    c.execute(command, (groupName,))
    selectedVal = c.fetchall()
    ans = [x[0] for x in selectedVal]
    db.close()
    return ans

def addGroupPic(username, picName, groupName):
    imgId = getImageId(username, picName)
    if imgId in getGroupPicIds(groupName):
        return False
    else:
        db = sqlite3.connect("data/draw.db")
        c = db.cursor()
        command = 'INSERT INTO groupPics VALUES(?, ?, ?);'
        c.execute(command, (imgId, groupName, 0))
        db.commit()
        db.close()
        return True
