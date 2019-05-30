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
    if loggedin():
        print("this is session:")
        print(session)
        return render_template("home.html", user = session['user'])
    return render_template("home.html")

@app.route("/register")
def register():
    if loggedin():
        return redirect(url_for("home"))
    return render_template("register.html")


def loggedin():
    if 'user' in session:
        return True
    else:
        return False

@app.route("/login", methods = ['POST','GET'])
def login():
    if loggedin():
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route('/logout')
def logout():
    if loggedin():
        session.pop('user')
    return redirect(url_for("home"))


@app.route('/mainDraw')
def mainDraw():
    if loggedin():
        return render_template("mainDraw.html")
    return redirect(url_for("home"))

#verify login
@app.route('/auth', methods=['POST','GET'])
def auth():
    print(request.method)
    username = request.form['username']
    password = request.form['password']
    if db.verifyUser(username,password):
        session['user'] = username
        return redirect(url_for("home"))
    else:
        flash('Username or Password is Incorrect')
        return redirect(url_for("login"))

@app.route('/adduser', methods=['POST','GET'])
def adduser():
    username = request.form['username']
    password = request.form['password']
    passwordc = request.form['confirm-password']
    if db.findUser(username) == True:
        flash ("Username already exists")
        return redirect(url_for("register"))
    if password != passwordc:
        flash ("Passwords don't match")
        return redirect(url_for("register"))
    db.registerUser(username,password)
    return redirect(url_for("home"))

@app.route('/myGroups')
def myGroups():
    if loggedin():
        return render_template("myGroups.html")
    return redirect(url_for("home"))

@app.route('/newGroup')
def newGroup():
    if loggedin():
        return render_template("newGroup.html")
    return redirect(url_for("home"))




if __name__ == '__main__':
    app.debug = True
app.run()
