#class example
class Flight:
    counter = 1
    def __init__(self, origin, destination, duration):
        # keep track of id
        self.id = Flight.counter
        Flight.counter += 1

        self.passengers = [] 

        self.origin = origin
        self.destination = destination
        self.duration = duration

    def delay (self, amount):
        self.duration += amount

    def add_passenger (self, passenger):
        self.passengers.append(passenger)
        passenger.flight_id = self.id 

    def print_info(self):
        print("Passengers:")
        for passenger in self.passengers:
            print(passenger.name)


class Passenger:
    def __init__(self, name):
        self.name = name


def main ():
    # create a flight
    f = Flight(origin="New Yotk", destination="Paris", duration=540)
    f.delay(10)

    david = Passenger(name = "David")
    alice = Passenger(name = "Alice")

    f.add_passenger(david)
    f.add_passenger(alice)

    f.print_info()
    
if __name__ == "__main__":
    main()


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