import os, csv, time, datetime, json

from flask import Flask, redirect, url_for, render_template, session, request, flash, get_flashed_messages

from urllib.request import Request, urlopen

from util import database as arms

# manage cookies and user data here
#instatiate users and pictures table if does not already exist
DB_FILE = "data/draw.db"
user = None
data = arms.DB_Manager(DB_FILE)
data.createLimitsTable()
data.createUsersTable()

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods=['POST','GET'])
def home():
    return render_template("home.html")

# @app.route("/register")
# def register():
#     if len(session) != 0:
#         return render_template("home.html", logged=True, user=list(session.items())[0][0])
#     return render_template("register.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
