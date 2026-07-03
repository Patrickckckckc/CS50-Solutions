from cs50 import SQL
from flask import Flask, redirect, render_template, request, session, url_for, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import os
from datetime import datetime

# Configure Application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/profile_image'

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///meditation.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


"""Pick between (Normal / Letting Go) Meditation, MAIN PAGE"""


@app.route("/")
def index():
    user_id = session.get("user_id")

    if user_id:
        rows = db.execute("SELECT username FROM users WHERE id = ?", user_id)
        username = rows[0]["username"] if rows else None

        # User’s own comments (include user_reaction)
        my_comments = db.execute("""
            SELECT comments.id,
                   comments.content,
                   comments.created_at,
                   comments.likes,
                   comments.dislikes,
                   reactions.reaction AS user_reaction
            FROM comments
            LEFT JOIN reactions
              ON reactions.comment_id = comments.id
             AND reactions.user_id = ?
            WHERE comments.user_id = ?
            ORDER BY comments.created_at DESC
        """, user_id, user_id)

        # Comments the user liked (include user_reaction)
        liked_comments = db.execute("""
            SELECT comments.id,
                   comments.content,
                   comments.created_at,
                   comments.likes,
                   comments.dislikes,
                   users.username,
                   reactions.reaction AS user_reaction
            FROM reactions
            JOIN comments ON reactions.comment_id = comments.id
            JOIN users ON comments.user_id = users.id
            WHERE reactions.user_id = ? AND reactions.reaction = 'like'
            ORDER BY comments.created_at DESC
        """, user_id)

    else:
        username = None
        my_comments = []
        liked_comments = []

    return render_template(
        "index.html",
        username=username,
        my_comments=my_comments,
        liked_comments=liked_comments
    )


""" Show Normal Meditation Page """


@app.route("/normal_meditation")
def normal_meditation():
    user_id = session.get("user_id")
    comments = db.execute("""
        SELECT comments.id,
               comments.user_id,
               comments.content,
               comments.created_at,
               users.username,
               comments.likes,
               comments.dislikes,
               (
                   SELECT reaction
                   FROM reactions
                   WHERE reactions.comment_id = comments.id
                     AND reactions.user_id = ?
               ) AS user_reaction
        FROM comments
        JOIN users ON comments.user_id = users.id
        WHERE comments.video_id = ?
        ORDER BY comments.created_at DESC
    """, user_id, 1)

    return render_template("normalmeditation.html", user_id=user_id, comments=comments)


""" Show Lettin Go Meditation Page """


@app.route("/lettingo_meditation")
def lettingo_meditation():
    user_id = session.get("user_id")
    comments = db.execute("""
        SELECT comments.id,
               comments.user_id,
               comments.content,
               comments.created_at,
               users.username,
               comments.likes,
               comments.dislikes,
               (
                   SELECT reaction
                   FROM reactions
                   WHERE reactions.comment_id = comments.id
                     AND reactions.user_id = ?
               ) AS user_reaction
        FROM comments
        JOIN users ON comments.user_id = users.id
        WHERE comments.video_id = ?
        ORDER BY comments.created_at DESC
    """, user_id, 2)

    return render_template("lettingo.html", user_id=user_id, comments=comments)


""" Add Comment with JavaScript """


@app.route("/add_comment", methods=["POST"])
def add_comment():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"success": False, "error": "Not logged in"})

    video_id = request.form.get("video_id")
    content = request.form.get("content", "").strip()

    if not content:
        return jsonify({"success": False, "error": "Content cannot be empty"})

    # Insert comment
    db.execute(
        "INSERT INTO comments (user_id, video_id, content, created_at, likes, dislikes) VALUES (?, ?, ?, CURRENT_TIMESTAMP, 0, 0)",
        user_id, video_id, content)

    # Get the new comment id
    new_comment = db.execute("SELECT last_insert_rowid() AS id")[0]["id"]

    username = db.execute("SELECT username FROM users WHERE id = ?", (user_id,))[0]["username"]

    return jsonify({
        "success": True,
        "id": new_comment,
        "username": username,
        "content": content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "likes": 0,
        "dislikes": 0,
        "owned": True
    })


""" Delete Comment with JavaScript """


@app.route("/delete_comment", methods=["POST"])
def delete_comment():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"success": False, "error": "Not logged in"})

    data = request.get_json()
    comment_id = data.get("comment_id")

    # Check if the comment belongs to the logged-in user
    comment = db.execute("SELECT user_id FROM comments WHERE id = ?", comment_id)
    if not comment or comment[0]["user_id"] != user_id:
        return jsonify({"success": False, "error": "Unauthorized"})

    # Delete the comment
    db.execute("DELETE FROM comments WHERE id = ?", comment_id)
    return jsonify({"success": True})


@app.route("/react_comment", methods=["POST"])
def react_comment():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"success": False, "error": "Not logged in"})

    data = request.get_json()
    comment_id = data.get("comment_id")
    action = data.get("action")  # "like" or "dislike"

    # Check if user already reacted
    existing = db.execute(
        "SELECT reaction FROM reactions WHERE user_id=? AND comment_id=?",
        user_id, comment_id
    )

    if existing:
        current = existing[0]["reaction"]
        if current == action:
            # Same reaction → remove (toggle off)
            db.execute("DELETE FROM reactions WHERE user_id=? AND comment_id=?", user_id, comment_id)
            if action == "like":
                db.execute("UPDATE comments SET likes = likes - 1 WHERE id=?", comment_id)
            else:
                db.execute("UPDATE comments SET dislikes = dislikes - 1 WHERE id=?", comment_id)
            user_reaction = None
        else:
            # Different reaction → update
            db.execute("UPDATE reactions SET reaction=? WHERE user_id=? AND comment_id=?",
                       action, user_id, comment_id)
            if current == "like":
                db.execute(
                    "UPDATE comments SET likes = likes - 1, dislikes = dislikes + 1 WHERE id=?", comment_id)
            else:
                db.execute(
                    "UPDATE comments SET dislikes = dislikes - 1, likes = likes + 1 WHERE id=?", comment_id)
            user_reaction = action
    else:
        # No reaction yet → insert new one
        db.execute("INSERT INTO reactions (user_id, comment_id, reaction) VALUES (?, ?, ?)",
                   user_id, comment_id, action)
        if action == "like":
            db.execute("UPDATE comments SET likes = likes + 1 WHERE id=?", comment_id)
        else:
            db.execute("UPDATE comments SET dislikes = dislikes + 1 WHERE id=?", comment_id)
        user_reaction = action

    # Get likes and dislikes
    counts = db.execute("SELECT likes, dislikes FROM comments WHERE id=?", comment_id)[0]
    likes = counts["likes"]
    dislikes = counts["dislikes"]

    return jsonify({
        "success": True,
        "likes": likes,
        "dislikes": dislikes,
        "user_reaction": user_reaction
    })


""" Show About Me Page """


@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")


""" Register Page """


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("register.html", message="Must Provide Username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("register.html", message="Must Provide Password")

        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return render_template("register.html", message="Must Provide Confirmation")

        # Ensure the password and confirmation are the same
        elif request.form.get("password") != request.form.get("confirmation"):
            return render_template("register.html", message="Different Passwords")

        # Add the user into the Database
        try:
            db.execute("INSERT INTO users (username, password_hash) VALUES (?,?)", request.form.get(
                "username"), generate_password_hash(request.form.get("password")))
        except ValueError or Exception:
            return render_template("register.html", message="Username Already Taken")

        # Remember which user has logged in
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("register.html")


""" Login Page """


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("login.html", message="Must Provide Username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("login.html", message="Must Provide Password")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["password_hash"], request.form.get("password")
        ):
            return render_template("login.html", message="Invalid username or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


""" Logout Page """


@app.route("/logout")
def logout():
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
