import sqlite3   # enable control of an sqlite database

class DB_Manager:
    '''
    HOW TO USE:
    Every method openDB by connecting to the inputted path of
    a database file. After performing all operations on the
    database, the instance of the DB_Manager must save using
    the save method.
    The operations/methods can be found below.
    '''
    def __init__(self, dbfile):
        '''
        SET UP TO READ/WRITE TO DB FILES
        '''
        self.DB_FILE = dbfile
        self.db = None
    #========================HELPER FXNS=======================
    def openDB(self):
        '''
        OPENS DB_FILE AND RETURNS A CURSOR FOR IT
        '''
        self.db = sqlite3.connect(self.DB_FILE) # open if file exists, otherwise create
        return self.db.cursor()

    def save(self):
        '''
        COMMITS CHANGES TO DATABASE AND CLOSES THE FILE
        '''
        self.db.commit()
        self.db.close()

    def isInDB(self, tableName):
        '''
        RETURNS True IF THE tableName IS IN THE DATABASE
        RETURNS False OTHERWISE
        '''
        c = self.openDB()
        command = 'SELECT * FROM sqlite_master WHERE type = "table"'
        c.execute(command)
        selectedVal = c.fetchall()
        # list comprehensions -- fetch all tableNames and store in a set
        tableNames = set([x[1] for x in selectedVal])

        return tableName in tableNames

    def table(self, tableName):
        '''
        PRINTS OUT ALL ROWS OF INPUT tableName
        '''
        c = self.openDB()
        command = 'SELECT * FROM "{0}"'.format(tableName)
        c.execute(command)

    def createUsersTable(self):
        '''
        CREATES A 3 COLUMN users table if it doesnt already exist. Used to store authentication info.
        '''
        c = self.openDB()
        if not self.isInDB('users'):
            command = 'CREATE TABLE "{0}"({1}, {2}, {3});'.format('users', 'username TEXT', 'password TEXT', 'banned INTEGER')
            c.execute(command)
        c.save()

    def createPicturesTable(self):
        '''
        CREATES A 5 COLUMN pictures table if it doesnt already exist. Used to store picture data.
        '''
        c = self.openDB()
        if not self.isInDB('pictures'):
            command = 'CREATE TABLE "{0}"({1}, {2}, {3}, {4}, {5});'.format('pictures', 'picId INTEGER', 'picName TEXT', 'username TEXT', 'caption TEXT', 'private INTEGER')
            c.execute(command)
        c.save()

#==========================================================
