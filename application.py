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

conn = sqlite3.connect("placeholder.db", check_same_thread=False)


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
