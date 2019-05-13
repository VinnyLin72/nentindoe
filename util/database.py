import sqlite3, api

#==========================================================
def init():
    db = sqlite3.connect("krispy.db")
    c = db.cursor()
    command = "CREATE TABLE IF NOT EXISTS user_info (username TEXT, password TEXT, address TEXT)"
    c.execute(command)
    db.commit()
    db.close()

#==========================================================
