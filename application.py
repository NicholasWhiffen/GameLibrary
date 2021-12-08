import sqlite3
from contextlib import closing
import imghdr
import os
from flask import Flask, render_template, redirect, request, abort, session, flash
from flask_session import Session
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/images'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jfif']
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
        with closing(conn.cursor()) as c:
            query = "SELECT * from Users WHERE Users.username = ?"
            c.execute(query, (request.form.get("username"),))
            user = c.fetchall()
        if user:
            if request.form.get("username") == user[1] and request.form.get("password") == user[2]:
                session["username"] = request.form.get("username")
                return redirect("/")
            elif request.form.get("username") != user[1] or request.form.get("password") != user[2]:
                flash("Incorrect username or password")
        else:
            flash("Username does not exist")
    return render_template("login.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    with closing(conn.cursor()) as c:
        query = "SELECT * from Users"
        c.execute(query)
        users = c.fetchall()
    if request.method == "POST":
        if users:
            if request.form.get("username") == user[1] and request.form.get("password") == user[2]:
                session["username"] = request.form.get("username")
                return redirect("/")
            elif request.form.get("username") != user[1] or request.form.get("password") != user[2]:
                flash("Incorrect username or password")
        else:
            flash("Username does not exist")
    return render_template("register.html")

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect("/")

@app.route("/collection", methods=["GET", "POST"])
def collection():
    with closing(conn.cursor()) as c:
        query = "SELECT * from Collections"
        c.execute(query)
        results = c.fetchall()
        games = []
        for result in results:
            games.append((result[1], result[2], result[3], result[4], result[5], result[6]))
    return render_template("collection.html", games=games)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/add", methods = ['POST'])
def getFormData():
    uploaded_file = request.files["file"]
    filename = secure_filename(uploaded_file.filename)
    title = request.values["title"]
    console = request.values["console"]
    year = request.values["year"]
    completed = request.values["completed"]
    rating = request.values["rating"]
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        with closing(conn.cursor()) as c:
            query = "INSERT into Collections(boxart, game_name, console, year, completed, rating) Values(?,?,?,?,?,?)"
            c.execute(query, (filename, title, console, year, completed, rating))
            conn.commit()
    return redirect("/collection")


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')