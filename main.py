from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3
import random

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
        return render_template("register.html")
    else:
        if "email" in session:
            return render_template("register.html")
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