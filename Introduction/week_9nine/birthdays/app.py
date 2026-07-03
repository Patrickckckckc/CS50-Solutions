import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        name, month, day = [request.form.get(x) for x in ["name", "month", "day"]]
        if not name or not month or not day:
            print("Missing Content")
            return redirect ("/")
        try:
            month = int(month)
            day = int(day)
        except:
            ValueError
            return redirect ("/")
        if not int(month) in range(1,13):
            print("Invalid Month")
            return redirect("/")
        elif  int(day) not in range(1, 32):
            print("Invalid Day")
            return redirect("/")

        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?,?,?)", name, month, day)
        return redirect("/")


    else:

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays = birthdays)


@app.route("/eliminated", methods=["POST"])
def eliminated():
    id = request.form.get("id")
    db.execute("DELETE FROM birthdays WHERE id = ?", id)
    return redirect("/")
