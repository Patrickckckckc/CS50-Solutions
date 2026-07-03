import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from Introduction.week_9nine.finance.helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # All stocks, shares, current_price, total
    stocks = db.execute("SELECT * FROM stocks WHERE user_id = ?", session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = float(cash[0]["cash"])
    stock_total = sum([float(stock["total"]) for stock in stocks])
    grand_total = cash + sum([float(stock["total"]) for stock in stocks])

    return render_template("index.html", stocks = stocks, cash = cash, stock_total = stock_total, grand_total = grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Look for the Stock
        stock = lookup(request.form.get("symbol"))
        try:
            shares = float(request.form.get("shares"))
        except ValueError:
            return apology("invalid shares", 400)

        # Check for Invalid Stock
        if stock == None:
            return apology("invalid stock", 400)
        elif shares <= 0:
            return apology("invalid number", 400)
        price = float(stock["price"])

        # Buy Transaction

        total = price * shares
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = float(cash[0]["cash"])

        # Check for valid buy
        if cash < total:
            return apology("not enough cash", 400)

        # Change Cash
        cash = cash - total
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        # Change Stock Table
        rows = db.execute(
            "SELECT * FROM stocks WHERE user_id = ? AND symbol = ?", session['user_id'], stock['symbol']
        )


        # If it´s already there
        if len(rows) == 1:
            # Correct the total, shares, and current_price
            new_total = total + float(rows[0]["total"])
            new_shares = shares + float(rows[0]["shares"])

            db.execute("UPDATE stocks SET current_price = ?, shares = ?, total = ? WHERE user_id = ? AND symbol = ? AND stock_name = ?", stock["price"], new_shares, new_total, session["user_id"], stock["symbol"], stock["name"])

        # If it´s new stock
        else:
            db.execute("INSERT INTO stocks (user_id, symbol, stock_name, current_price, shares, total) VALUES (?,?,?,?,?,?)", session["user_id"], stock["symbol"], stock["name"], stock["price"], shares, total)

        # Actualize History Table
        db.execute("INSERT INTO history (user_id, symbol, action, transaction_shares, current_price) VALUES (?, ?, ?, ?, ?)", session["user_id"], stock["symbol"], 'buy', shares, stock["price"])

        return redirect("/")

    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    stocks = db.execute("SELECT * FROM history WHERE user_id = ?", session["user_id"])
    return render_template("history.html", stocks = stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        # Look for the Stock
        stock = lookup(request.form.get("symbol"))

        # Check for Invalid Stock
        if stock == None:
            return apology("invalid stock", 403)

        return render_template("quoted.html", stock = stock)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 403)

        # Ensure the password and confirmation are the same
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("different passwords", 403)

        # Add the user into the Database
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?,?)", request.form.get("username"), generate_password_hash(request.form.get("password")))
        except ValueError:
            return apology("Username already taken", 403)

        # Remember which user has logged in
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        # Look for the Stock
        stock = lookup(request.form.get("symbol"))
        try:
            shares = float(request.form.get("shares"))
        except ValueError:
            return apology("invalid shares", 400)

        # Check for Invalid Stock and Shares
        if stock == None:
            return apology("invalid stock", 400)
        elif shares <= 0:
            return apology("invalid number", 400)

        # Sell Transaction
        # Check if the user owns STOCK and VALID SHARES
        rows = db.execute("SELECT * FROM stocks WHERE user_id = ? AND symbol = ?", session['user_id'], stock['symbol'])

        # Stock not in the table
        if len(rows) != 1:
            return apology("stock not in account", 400)

        # Not enough SHARES
        shares_own = rows[0]["shares"]
        if shares_own <= 0 or shares > shares_own:
            return apology("not enough shares", 400)

        # Change Cash
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = float(cash[0]["cash"])
        cash = cash + (shares * float(stock["price"]))
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        # Change Stock Table SHARES
        shares_own = shares_own - shares

        # If its 0 delete
        if shares_own == 0:
            db.execute("DELETE FROM stocks WHERE user_id = ? AND symbol = ?", session["user_id"], stock["symbol"])
        else:
            new_total = float(rows[0]["total"]) - (shares * float(stock["price"]))
            db.execute("UPDATE stocks SET shares = ?, total = ? WHERE user_id = ? AND symbol = ?", shares_own, new_total, session["user_id"], stock["symbol"])

        # Actualize History Table
        db.execute("INSERT INTO history (user_id, symbol, action, transaction_shares, current_price) VALUES (?, ?, ?, ?, ?)", session["user_id"], stock["symbol"], 'sell', shares, stock["price"])

        return redirect("/")

    else:
        return render_template("sell.html")
