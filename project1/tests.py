
import csv
import os
import requests

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():  
    """
    # add a book to the database
    isbn = "other example"
    title = "Other title"
    author = "Other author"
    year = 2001
    db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                        {"isbn": isbn , "title": title, "author": author, "year": year} )
    db.commit()
    """

    """
    # add a user to the database
    name = "Daniel"
    password = "lalala"
    db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
                        {"username": name , "password": password} )
    db.commit()
    """

    """
    # add a review to the database
    book_isbn = "exampleISBN"
    rating = 5
    text = "Very good"
    user_id = 2
    db.execute("INSERT INTO reviews (book_isbn, rating, text, user_id) VALUES (:book_isbn, :rating, :text, :user_id)",
                        {"book_isbn":book_isbn , "rating": rating, "text": text, "user_id":user_id} )
    db.commit()
    """

    """
    # list all users:
    users = db.execute("SELECT id, username, password FROM users LIMIT 10").fetchall()
    for user in users:
        print(f"id: {user.id} | username: {user.username} | pasword: {user.password}")

    # list all books:
    books = db.execute("SELECT isbn, title, author, year FROM books").fetchall()
    for book in books:
        print(f"isbn: {book.isbn} | title: {book.title} | author: {book.author} | year: {book.year}")
    """
    """
    # list all reviews:
    reviews = db.execute("SELECT id, book_isbn, rating, text, user_id FROM reviews").fetchall()
    for review in reviews:
        print(f"id: {review.id} | isbn: {review.book_isbn} | rating: {review.rating} | text: {review.text} | user id: {review.user_id}")
    """

    """
    # search for the text:
    txt="Kro"
    txt = "%" + txt + "%"
    print(txt)
    books = db.execute("SELECT * FROM books WHERE isbn LIKE :isbn OR title LIKE :title OR author LIKE :author", 
        {"isbn": txt, "title": txt, "author": txt}).fetchall()
    
    for book in books:
        print(f"isbn: {book.isbn} | title: {book.title} | author: {book.author} | year: {book.year}")
    """

    """
    # search for the isbn:
    isbn = "0380811081"
    book = db.execute("SELECT * FROM books WHERE isbn = :isbn ", 
        {"isbn": isbn}).fetchone()

    print(f"isbn: {book.isbn} | title: {book.title} | author: {book.author} | year: {book.year}")
    """
    
    """
    # get the reviews:
    isbn = "0380795272"
    reviews = db.execute("SELECT * FROM reviews WHERE book_isbn = :isbn",
        {"isbn": isbn}).fetchall()
    for review in reviews:
        print(f"id: {review.id} | isbn: {review.book_isbn} | rating: {review.rating} | text: {review.text} | user id: {review.user_id}")
    """

    """
    user_id = 5
    isbn = "0380795272"
    rating = 5
    text = "This book is excelent"

    if db.execute("SELECT * FROM reviews WHERE book_isbn = :isbn AND user_id = :user_id",
        {"isbn": isbn, "user_id": user_id}).rowcount == 0:
        db.execute("INSERT INTO reviews (book_isbn, rating, text, user_id) VALUES (:book_isbn, :rating, :text, :user_id)",
            {"book_isbn": isbn , "rating": rating, "text": text, "user_id":user_id} )
        db.commit()
    else:
        print("you have already reviewed this book")
    """
    """
    key="MW2WkG1pV99eR1unviQTdw" 
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": key, "isbns": "9781632168146"})
    
    review = res.json()

    count = review ["books"][0]["work_ratings_count"]
    average = review ["books"][0]["average_rating"]

    print(f"count: {count} average: {average}")
    """ 

if __name__ == "__main__":
    main()




#---------- NOTES ---------------------:

# TABLES: (OLD!)

# books:
#   - isbn
#   - title
#   - author
#   - publication_year

# users:
#   - id
#   - username
#   - password

# revisions:
#   - id
#   - rating (1-5)
#   - text

"""
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL
);

CREATE TABLE books (
    isbn VARCHAR PRIMARY KEY,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    year INTEGER NOT NULL
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    book_isbn VARCHAR REFERENCES books,
    rating INTEGER NOT NULL,
    text VARCHAR NOT NULL,
    user_id INTEGER REFERENCES users
);

-- commands to Adminer:
SELECT * FROM "users" WHERE username='David' -> worked on Adminer


-- commands in postgre:

INSERT INTO books (isbn, title, author, year) 
VALUES ('exampleISBN', 'Example title', 'example author', 1982);

INSERT INTO users (username,password) 
VALUES ('John' , 'lololol');

# e.g:  0380795272,Krondor: The Betrayal,Raymond E. Feist,1998

INSERT INTO reviews (book_isbn, rating, text, user_id)
VALUES ('0380795272', 5, 'very good', 2);

DELETE FROM books WHERE year = '1998';

SELECT isbn, title, author, year, rating, text, user_id FROM books 
INNER JOIN reviews ON reviews.book_isbn = books.isbn;

SELECT * FROM books
WHERE isbn LIKE '%as%' OR title LIKE '%as%' OR author LIKE '%as%' ; 

SELECT * FROM reviews WHERE book_isbn = '0380795272';

"""

""" diferent pages:
- layout 

- index.html (log in or register)
- register.html (registration) 
- search.html (once your are inside)
- book.html (all data | reviews | option to submit a new review)
            (also data from goodreads)
            
"""

# GOODREADS:

# key: MW2WkG1pV99eR1unviQTdw
# secret: Wq3YWM0WVi0JuZW3YUCcfknuZVF20t0T84SyD6U
