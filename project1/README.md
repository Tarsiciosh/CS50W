# CS50W - project 1

# WIN
- cd C:\Users\spa3cap\Github\flask (0)
- py -3 -m venv venv
- venv\Scripts\activate (1)
- python -m pip install --upgrade pip
- pip3 install -r requirements.txt
- cd C:\Users\spa3cap\Documents\GitHub\project1 (2)
- set FLASK_APP=application.py (3)
- set FLASK_ENV=development (4)
- set DATABASE_URL=postgres://ykdikqxszzjfkx:91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d9ctctlaucdee0 (5)
- flask run (6)

# MAC (checked)
- cd /users/Tar/frameworks/flask (0)
- python3 -m venv venv
- . venv/bin/activate (1)
- python -m pip install --upgrade pip
- pip3 install -r requirements.txt
- cd /users/Tar/github/CS50W/project1 (2)
- export FLASK_APP=application.py (3)
- export FLASK_ENV=development (4)
- export DATABASE_URL=postgres://ykdikqxszzjfkx:91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d9ctctlaucdee0 (5)
- flask run (6)


# DATABASE CREDENTIALS:
- host: ec2-54-152-175-141.compute-1.amazonaws.com
- database: d9ctctlaucdee0
- user: ykdikqxszzjfkx
- port: 5432
- password: 91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a
- URI: postgres://ykdikqxszzjfkx:91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d9ctctlaucdee0

# IN PC
- cd C:\Program Files\PostgreSQL\12\bin\ (win)
- export PATH=/Library/PostgreSQL/12/bin/:$PATH (mac)
- psql postgres://ykdikqxszzjfkx:91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d9ctctlaucdee0

# GOODREADS:
- key: MW2WkG1pV99eR1unviQTdw
- secret: Wq3YWM0WVi0JuZW3YUCcfknuZVF20t0T84SyD6U
