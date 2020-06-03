# lecture8
CS350W lecture 8 CI-CD

# test is_prime manually:
(shell)

# test is_prime with other function:
(tests0.py - test_prime)
(tests0.sh)

# test is_prime with asserts:
(assert0.py)
(assert1.py)

# test is_prime with unittest:
(tests1.py)

# test in django (airline1):
(models.py - is_valid_flight)
(test.py)
...
self.assertTrue(f.is_valid_flight())
...

# test the models (airline1 - didn't work):
(flights/models.py - Flight class)
- check data before saving it in the db:


def clean(self):
    if self.origin == self.destination:
        raise ValidationError("Origin and destination must be different.")
    elif self.duration < 1:
        raise ValidationError("Duration must be positive.")
def save(self, *-args, **-kwargs) :
    self.clean()

    # This syntax now calls Django's own "save" function, adding this data to the DB (if `clean` was ok).
    super().save(*-args, **-kwargs)

(note: remove the "-" after the star)

# test the views (airline2):
(flights/tests.py)
...
def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["flights"].count(), 2)
...
>> python manage.py test

# selenium:
> cd c:\Users\spa3cap\Documents\GitHub\django
> venv\Scripts\activate
>> pip install selenium
- download the geckodriver for firefox
- put it in C:\WebDriver\bin
> setx /m path "%path%;C:\WebDriver\bin\"
>> python manage.py test

# CI-CD (airline3)
- crate a travis account linked with github
(/.travis.yml - create)
language: python
python:
    - 3.6
install:
    - pip install -r requirements.txt
script:
    - python manage.py test

- commit changes and see the result-

# Heroku (ariline3 - didn't work)
- follow the instructions of the class note
settings (avatar) > account


# Docker (airline4)
- install docker desktop
- add it to the PATH (windows)
cd c:\Users\spa3cap\Documents\GitHub\lecture8\airline4
> docker-compose up
go to 0.0.0.0:8000 to see the running website
> docker ps (list the current docker containers)
> docker exec -it <containerid> bash -l
root@dfj..> python manage.py shell (for example)

#
