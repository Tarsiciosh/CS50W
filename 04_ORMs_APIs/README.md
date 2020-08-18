# lecture4
lecture 4 of CS350

$ cd C:\Users\spa3cap\Documents\GitHub\project1 (0)
$ py -3 -m venv venv (install virtual enviroment)
$ venv\Scripts\activate (activate) (1)
$ python -m pip install --upgrade pip (update pip)
$ pip3 install -r requirements.txt (intall all from project1)
$ set FLASK_APP=application.py (2)
$ set FLASK_ENV=development (3)
$ set DATABASE_URL=postgres://ykdikqxszzjfkx:91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d9ctctlaucdee0 (4)
$ flask run (5)

# DATABASE CREDENTIALS:
- host: ec2-54-152-175-141.compute-1.amazonaws.com
- database: d9ctctlaucdee0
- user: ykdikqxszzjfkx
- port: 5432
- password: 91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a
- URI: postgres://ykdikqxszzjfkx:91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d9ctctlaucdee0

$ cd C:\Program Files\PostgreSQL\12\bin\
$ psql postgres://ykdikqxszzjfkx:91e70af3b6523523b349c7a70564e385f1c1c56e431ce9177c6e0608ff1b2f4a@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d9ctctlaucdee0

