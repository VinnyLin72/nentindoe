import os, csv, time, datetime, sqlite3, json

from flask import Flask, redirect, url_for, render_template, session, request, flash, get_flashed_messages

from urllib.request import Request, urlopen


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
