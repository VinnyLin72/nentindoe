import os, csv, time, sqlite3, datetime, json

from flask import Flask, redirect, url_for, render_template, session, request, flash, get_flashed_messages

from urllib.request import Request, urlopen

from util import database as arms

# manage cookies and user data here
#instatiate users and pictures table if does not already exist
'''
DB_FILE = "data/draw.db"
user = None
data = arms.DB_Manager(DB_FILE)
data.createLimitsTable()
data.createUsersTable()
'''
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods=['POST','GET'])
def home():
    if loggedin():
        return render_template("home.html", logged = True)
    return render_template("home.html")

@app.route("/register")
def register():
    if loggedin():
        return redirect(url_for("home"))
    return render_template("register.html")


def loggedin():
    if len(session) != 0:
        return True
    else:
        return False

@app.route("/login")
def login():
    if loggedin():
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop()
    return redirect(url_for("home"))

@app.route('/mainDraw')
def mainDraw():
    if loggedin():
        return render_template("mainDraw.html")
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.debug = True
    app.run()
