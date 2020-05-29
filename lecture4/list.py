import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    flights = Flight.query.all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")
    
    # example of filter:
    f = Flight.query.filter_by(origin="Paris").first()
    print(f"the flight: {f.origin} to {f.destination} takes {f.duration} minutes.")
    
    # example of count:
    count = Flight.query.filter_by(origin="Paris").count()
    print(f"there are {count} flights from Paris")

    # filter by the key:
    Flight.query.filter_by(id=1).first() # is the same as:
    Flight.query.get(1)

    # example of update:
    flight = Flight.query.get(1)
    flight.duration = 120

    """
    # example of delete: 
    flight = Flight.query.get(4)
    db.session.delete(flight)
    """
    # example of order:
    flights = Flight.query.order_by(Flight.origin.desc()).all()

    # example of filter:
    flights = Flight.query.filter(Flight.origin != "Paris").all()

    # example of like:
    flights = Flight.query.filter(Flight.origin.like("%Pa%")).all()

    # example of in:
    flights = Flight.query.filter(Flight.origin.in_(["Paris","Tokyo"])).all()

    # example of join:
    m = db.session.query(Flight,Passenger).filter(Flight.id == Passenger.flight_id).all()

    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration}")
    
    db.session.commit()

    print(m)
    

if __name__ == "__main__":
    with app.app_context():
        main()
