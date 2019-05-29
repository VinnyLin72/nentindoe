#!/usr/bin/python3.6
import os, csv, time, sqlite3, datetime, json

from flask import Flask, redirect, url_for, render_template, session, request, flash, get_flashed_messages

from urllib.request import Request, urlopen

from util import database as db

# manage cookies and user data here
#instatiate users and pictures table if does not already exist

#-------------------------------------------------------------------------------
#Testing DB Stuff
db.init()
#print(db.registerUser("a","a"))
# print(db.registerUser("a","b"))

#-------------------------------------------------------------------------------


app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods=['POST','GET'])
def home():
    return render_template("oauthtest.html")

if __name__ == '__main__':
    app.debug = True
app.run()
