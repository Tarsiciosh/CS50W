import os
import requests
from flask import Flask, render_template, jsonify, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    username = request.form.get("username")
    password = request.form.get("password")
    user = db.execute("SELECT * FROM users WHERE username = :username AND password = :password", 
        {"username": username, "password": password}).fetchone()
    # validate login:
    if user is None:
        return render_template("error.html", message="username or password don't match")
    else:   
        my_id = user.id
        print(f"my id is {my_id}")
        return render_template("search.html")  

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/validate_register", methods=["POST"])
def validate_register():
    username = request.form.get("username")
    password = request.form.get("password")
    # Make sure username does not exist:
    if db.execute("SELECT * FROM users WHERE username = :username", {"username": username}).rowcount == 0:   
        db.execute("INSERT INTO users (username, password) VALUES (:username, :password)", {"username": username , "password": password})
        db.commit() 
        return render_template("success.html", message="you are registered")
    else:
        return render_template("error.html", message="username already exist")

@app.route("/book_list", methods=["POST"])
def book_list():
    txt = request.form.get("txt")
    txt = "%" + txt + "%"
    books = db.execute("SELECT * FROM books WHERE isbn LIKE :isbn OR title LIKE :title OR author LIKE :author", 
        {"isbn": txt, "title": txt, "author": txt}).fetchall()
    if books is None: # or book.length == 0:
        return render_template ("error.html", message ="no books")
    else:
        return render_template ("books.html", books=books)

@app.route("/book/<string:isbn>")
def book(isbn):
    # search for that isbn and get the book:
    book = db.execute("SELECT * FROM books WHERE isbn = :isbn ", 
        {"isbn": isbn}).fetchone()
   
    # search for the reviews and get the reviews:
    reviews = db.execute("SELECT * FROM reviews WHERE book_isbn = :isbn",
        {"isbn": isbn}).fetchall()
    
    if reviews is None:
        reviews = "There are no reviews"

    # goodreads data:
    key="MW2WkG1pV99eR1unviQTdw" 
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={
        "key": key, "isbns": isbn})
    review = res.json()
    count = review ["books"][0]["work_ratings_count"]
    average = review ["books"][0]["average_rating"]

    if book is None:
        return render_template("error.html", message="error ocurred")
    else:
        return render_template ("book.html", book=book, reviews= reviews, count= count, average= average)

@app.route("/add_review/<string:isbn>", methods=["POST"])
def add_review(isbn):
    # get the form text and rating:
    text = request.form.get("text")
    rating = request.form.get("rating")
    user_id = 13
    # add the review:
    if db.execute("SELECT * FROM reviews WHERE book_isbn = :isbn AND user_id = :user_id",
        {"isbn": isbn, "user_id": user_id}).rowcount == 0:
        db.execute("INSERT INTO reviews (book_isbn, rating, text, user_id) VALUES (:book_isbn, :rating, :text, :user_id)",
            {"book_isbn": isbn , "rating": rating, "text": text, "user_id":user_id} )
        db.commit()
        return render_template("success.html", message="review added")
    else:
        return render_template("error.html", message="sorry, you have already reviewed this book")

@app.route("/api/<string:isbn>")
def api(isbn):
    book = db.execute("SELECT * FROM books WHERE isbn = :isbn ", 
        {"isbn": isbn}).fetchone()

    if book is None:
        return jsonify({"error": "no such isbn"}), 404

    reviews = db.execute("SELECT * FROM reviews WHERE book_isbn = :isbn",
        {"isbn": isbn}).fetchall()
    
    count = 0
    average = 0

    for review in reviews:
        average += review.rating 
        count += 1

    if count > 0 :
        average /= count

    return jsonify ({
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "isbn": book.isbn,
        "reviews_count": count,
        "average_score": average
    })


# cd C:\Users\spa3cap\Documents\GitHub\project1 (0)
# py -3 -m venv venv (install virtual enviroment)
# venv\Scripts\activate (activate) (1)
# python -m pip install --upgrade pip (update pip)
# pip3 install -r requirements.txt (intall all from project1)
# set FLASK_APP=application.py (2)
# set FLASK_ENV=development (3)
# set DATABASE_URL=postgres://ykdikqxszzjfkx:91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d9ctctlaucdee0 (4)
# flask run (5)

# DATABASE CREDENTIALS:
# host: ec2-54-152-175-141.compute-1.amazonaws.com
# database: d9ctctlaucdee0
# user: ykdikqxszzjfkx
# port: 5432
# password: 91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a
# URI: postgres://ykdikqxszzjfkx:91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d9ctctlaucdee0

# cd C:\Program Files\PostgreSQL\12\bin\
# psql postgres://ykdikqxszzjfkx:91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d9ctctlaucdee0

# GOODREADS:
# key: MW2WkG1pV99eR1unviQTdw
# secret: Wq3YWM0WVi0JuZW3YUCcfknuZVF20t0T84SyD6U