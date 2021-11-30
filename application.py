import sqlite3
from contextlib import closing
import imghdr
import os
from flask import Flask, render_template, redirect, request, abort, session
from flask_session import Session
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

conn = sqlite3.connect("collections.db", check_same_thread=False)


@app.route("/")
def index():
    if not session.get("username"):
        return redirect("/login")
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect("/")
    return render_template("login.html")


@app.route("/collection", methods=["GET", "POST"])
def collection():
    with closing(conn.cursor()) as c:
        query = "SELECT * from Collections"
        c.execute(query)
        results = c.fetchall()
        games = []
        for result in results:
            games.append((result[1], result[2], result[3], result[4], result[5], result[6]))
    return render_template("photos.html", games=games)
