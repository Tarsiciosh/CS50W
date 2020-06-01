# Project 1

Web Programming with Python and JavaScript

(win)
- cd C:\Users\spa3cap\Documents\GitHub\project1 (0)
- py -3 -m venv venv
- venv\Scripts\activate (1)
- python -m pip install --upgrade pip
- pip3 install -r requirements.txt
- set FLASK_APP=application.py (2)
- set FLASK_ENV=development (3)
- set DATABASE_URL=postgres://ykdikqxszzjfkx:91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d9ctctlaucdee0
- flask run (5)

(mac)
- cd users/Tar/frameworks/flask
- python3 -m venv venv
- . venv/bin/activate
- python -m pip install --upgrade pip
- pip3 install -r requirements.txt
- cd github/CS50W/project1
- export FLASK_APP=application.py
- export FLASK_ENV=development
- export DATABASE_URL=postgres://ykdikqxszzjfkx:91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d9ctctlaucdee0 (4)
- flask run


# DATABASE CREDENTIALS:
# host: ec2-54-152-175-141.compute-1.amazonaws.com
# database: d9ctctlaucdee0
# user: ykdikqxszzjfkx
# port: 5432
# password: 91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a
# URI: postgres://ykdikqxszzjfkx:91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d9ctctlaucdee0

# cd C:\Program Files\PostgreSQL\12\bin\
- export PATH=/Library/PostgreSQL/12/bin/:$PATH (mac)
# psql postgres://ykdikqxszzjfkx:91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d9ctctlaucdee0

# GOODREADS:
# key: MW2WkG1pV99eR1unviQTdw
# secret: Wq3YWM0WVi0JuZW3YUCcfknuZVF20t0T84SyD6U
