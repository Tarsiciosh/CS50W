import os
from flask import Flask, render_template, jsonify, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)


@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    # Get form information.
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    # Make sure the flight exists.
    flight = Flight.query.get(flight_id)
    if not flight:
        return render_template("error.html", message="No such flight with that id.")

    # Add passenger.
    flight.add_passenger(name)
    return render_template("success.html")


@app.route("/flights")
def flights():
    """List all flights."""
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about a single flight."""

    # Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight.")

    # Get all passengers.
    passengers = flight.passengers
    return render_template("flight.html", flight=flight, passengers=passengers)


@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    """Return details about a single flight."""

    # Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return jsonify({"error": "Invalid flight_id"}), 422

    # Get all passengers.
    passengers = flight.passengers
    names = []
    for passenger in passengers:
        names.append(passenger.name)
    return jsonify({
            "origin": flight.origin,
            "destination": flight.destination,
            "duration": flight.duration,
            "passengers": names
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
