from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3
import random
from uuid import uuid4
from cryptography.fernet import Fernet

key = b'alerr8icGEY6tbt3qvLWg5hJU6C_BIeCIQ5_zZzwWOM='
cipher_suite = Fernet(key)

app = Flask(__name__)
app.secret_key = "Testing"


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        return render_template("index.html")
    else:
        if "email" in session:
            return render_template("index.html")
        else:
            return render_template("index.html")

@app.route("/forums/", methods=["POST", "GET"])
def forums():
    if request.method == "POST":
        return render_template("forums.html")
    else:
        if "email" in session:
            return render_template("forums.html")
        else:
            return render_template("forums.html")

@app.route("/register/", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        password = request.form['password']
        email = request.form['email']
        username = request.form['username']
        db = sqlite3.connect('main.db')
        cursor = db.cursor()
        cursor.execute("SELECT email FROM users WHERE email = '{}'".format(email))
        result = cursor.fetchone()
        if result is not None:
            return redirect(url_for("login"))
        else:
            auth_token = uuid4()
            pas = cipher_suite.encrypt(bytes(password, encoding='utf8'))
            sql = ("INSERT INTO users(email, username, password, confirmed, pfp, bio, perms, friends, token) VALUES(?,?,?,?,?,?,?,?)")
            val = (str(email),str(username), pas, False, "N/A", "N/A", "N/A", "N/A", str(auth_token))
            cursor.execute(sql, val)
            db.commit()
            session["user"] = username
            session["email"] = email
            return redirect(url_for("login"))
        cursor.close()
        db.close()
    else:
        if "email" in session:
            return render_template("index.html")
        else:
            return render_template("register.html")

@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return render_template("login.html")
    else:
        if "email" in session:
            return render_template("login.html")
        else:
            return render_template("login.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)