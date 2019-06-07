#!/usr/bin/python3.6
import os, csv, time, sqlite3, datetime, json

from flask import Flask, redirect, url_for, render_template, session, request, flash, get_flashed_messages

from urllib.request import Request, urlopen

from util import database as db

from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import google_auth

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

app.register_blueprint(google_auth.app)




@app.route('/', methods=['POST','GET'])
def home():
    if loggedin():
        print("this is session:")
        print(session)
        return render_template("home.html", user = session['user'])
    return render_template("home.html")


@app.route('/oauth')
def oauth():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
        return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"

    return 'You are not currently logged in.'


@app.route("/register")
def register():
    if loggedin():
        return redirect(url_for("home"))
    return render_template("register.html")


# def loggedin():
#     if 'user' in session:
#         return True
#     else:
#         return False

def loggedin():
    return google_auth.is_logged_in()

# @app.route("/login", methods = ['POST','GET'])
# def login():
#     if loggedin():
#         return redirect(url_for("home"))
#     return render_template("login.html")

@app.route("/login", methods = ['POST','GET'])
def login():
    if loggedin():
        return redirect(url_for("home"))
    return redirect('/google/login')

# @app.route('/logout')
# def logout():
#     if loggedin():
#         session.pop('user')
#     return redirect(url_for("home"))

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect('/google/logout')


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
        my_groups=db.getJoined(session['user'])
        return render_template("myGroups.html", groupList = my_groups)
    return redirect(url_for("home"))

@app.route('/newGroup')
def newGroup():
    if loggedin():
        return render_template("newGroup.html")
    return redirect(url_for("home"))

@app.route('/newGroupAuth', methods=["POST","GET"])
def newGroupAuth():
    if loggedin():
        groupname=request.form["groupName"]
        db.createGroup(session['user'],groupname)
        return redirect(url_for("myGroups"))
    return redirect(url_for("home"))

@app.route('/viewGroup', methods = ["POST","GET"])
def viewGroup():
    if loggedin():
        groupName=request.form["groupName"]
        print("groupname")
        print(groupName)
        picIds= db.getGroupPicIds(groupName)
        return render_template("groupPage.html",groupPics=picIds)
    return redirect(url_for("home"))

@app.route('/myDrawings')
def myDrawings():
    if loggedin():
        myPics= db.getPictures(session['user'])
        imgIds=[]
        return render_template("myDrawings.html", imglist=myPics)
    return redirect(url_for("home"))

@app.route('/save', methods=["POST","GET"])
def save():
    if loggedin():
        iurl=request.form["imgurl"]
        print(session['user'])
        db.saveImage(iurl,session['user'])
        myPics=db.getPictures(session['user'])
        print(myPics)
        return redirect(url_for("myDrawings"))
    return redirect(url_for("home"))







if __name__ == '__main__':
    app.debug = True
app.run()
