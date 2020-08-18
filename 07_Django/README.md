Hello this is a readme file for the CS350 class
Lecture 7:

# First steps:

$ cd C:\Users\spa3cap\Documents\GitHub\django (0)
$ py -3 -m venv venv (install virtual enviroment)
$ venv\Scripts\activate (activate) (1)
$ python -m pip install --upgrade pip (update pip)
$ pip install Django==3.0.6
$ cd c:\Users\spa3cap\Documents\Github\lecture7\djangoair

# Walk through:

django-admin startproject djangoair (creates a project)
cd djangoair
python manage.py startapp flights (creates an app)

(flights/urls.py - create)
from django.urls import path 
from . import views # "." same directory 
urlpatterns = [
    path("", views.index),
]

(flights/views.py)
from django.http import HttpResponse
from django.shortcuts import render
def index (request):
    return HttpResponse("Flights")

(djangoair/urls.py)
from django.urls import include
urlpatterns = [
    path('', include('flights.urls')),
    path('admin/', admin.site.urls),
]

(flights/models.py)
class Flight(models.Model): #inherits from models.Model
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

(dajangoair/settings.py) (registration of the app)
INSTALLED_APPS = [
    'flights.apps.FlightsConfig',
     'django.contrib.admin',
     ...

# MIGRATIONS:
> python manage.py makemigrations
migrations/0001_initial.py(created) 
> python manage.py sqlmigrate flights 0001 (to see the generated code for the data base)
> python manage.py migrate (create everything really)

(djangoair/settings.py) (to see the databases - here a file with sqlite)
DATABASES (dictionary)
db.sqlite3 (file)

# DAJANGO SHELL:
> python manage.py shell
> from flights.models import Flight
> f = Flight (origin="Buenos Aires", destination="Munich", duration=415)
> f.save()
> Flight.objects.all() 
    <QuerySet [<Flight: Flight object (1)>]>

(flights/models.py) 
def __str__(self):
    return f"{self.id} - {self.origin} to {self.destination}: {self.duration}"
> f = Flight.objects.first() or .last()
> f.origin
> f.delete()

# BETTER MODELS:
(models.py)
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.city} ({self.code})"

in Flight:
 origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")

|- migrate the changes -|

> jfk = Airport(code="JFK", city="New York City")
> lhr = Airport(code="LHR", city="London")
> jfk.save()
> lhr.save()
> f = Flight(origin=jfk, destination=lhr, duration=415)
> f.save()
> f.origin.code
> jfk.departures.all()

# RENDERING TEMPALTES:
(flights/views.py)
from .models import Flight
def index (request):
    context = {
        "flights": Flight.objects.all()
    }
    return render (request, "flights/index.html", context)

(templates/flights/index.html - create)
<!DOCTYPE html>
<html> 
    <head>
        <title>Flights</title>
    </head>
    <body>
        <h1>Flights</h1>
        <ul>
            {% for flight in flights %}
                <li>
                    {{ flight }}
                </li>
            {% endfor %}
        </ul>
    </body>
</html>

# ADMIN:
(flights/admin.py)
from .models import Airport, Flight
admin.site.register(Airport)
admin.site.register(Flight)
> python manage.py createsuperuser
> user: spa3cap
> pass: Bambilandia
run the server and then access the admin route

# ADDING MORE ROUTES:
(flights/urls.py)
path ("<int:flight_id>", views.flight)

(views.py)
from django.http import Http404

def flight(request,flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id) # primary key
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")
    context = {
        "flight": flight,
    }
    return render (request, "flights/flight.html",context)

(templates/flights/flight.html - create)
<!DOCTYPE html>
<html> 
    <head>
        <title>{{ flight.id }}</title>
    </head>
    
    <body>
        <h1> {{ flight.id }}  </h1>
        
        <p>Origin: {{ flight.origin }} </p>
        <p>Estination: {{ flight.destination }} </p>
    </body>

</html>

# TEMPLATE INHERITANCE:
(templates/base.html - create)
<!DOCTYPE html>
<html>
    <head>
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
        {% block body %}
        {% endblock %}
    </body>
</html>

(template/index.html)
{% extends "flights/base.html" %}
{% block title %}
    Flights
{% endblock %}
{% block body %}
    <h1>Flights</h1>
    <ul>
    {% for flight in flights %}
        <li> <a href="{% url 'flight' flight.id %}">{{ flight }}</a> </li>
    {% endfor %}
    </ul>
{% endblock %}

(template/flight.html)
{% extends "flights/base.html" %}
{% block title %}
    Flight {{ flight.id }}
{% endblock %}
{% block body %}
    <h1>Flight {{ flight.id }}</h1>
    <ul>
        <li>Origin: {{ flight.origin }}</li>
        <li>Destination: {{ flight.destination }}</li>
    </ul>
    <a href="{% url 'index' %}">Back to full listing</a>
{% endblock %}

(flights/urls)
, name="index"),
, name="flight")

# MODEL RELATIONSHIPS:
(flights/models.py)
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    def __str__(self):
        return f"{self.first} {self.last}"

> python manage.py makemigrations
> python manage.py sqlmigrate flights 0003
> from flights.models import Flight, Passenger
> f = Flight.objects.get(pk=1)
> p = Passenger(first="Alice", last="Adams")
> p.save()
> p.flights.add(f)
> p.flights.all()
> f.passengers.all()

(flights/views.py)
context
"passengers": flight.passengers.all()

(flights/templates/fliht.html)
<h2>Passengers</h2>
    <ul>
        {% for passenger in passengers %}
            <li>{{ passenger }}</li>
        {% empty %}
            <li>No passengers</li>
        {% endfor %}
    </ul>

# USER REGISTRATON (BOOK):
(flights/urls.py)
 path("<int:flight_id>/book", views.book, name="book")

(flight/views.py)
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger

def book(request, flight_id):
    try:
        passenger_id = int (request.POST["passenger"])
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=passenger_id)
    except KeyError:
        return render(request, "flights/error.html", {"message": "No selection."})
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No flight."})
    except Passenger.DoesNotExist:
        return render(request, "flights/error.html", {"message: No Passenger"})
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

(in the context of the function flight) 
"non_passengers": Passenger.objects.exclude(flights= flight).all()

(flitghts/flight.html)
 {% if non_passengers %}
    <h2>Add a Passenger</h2>
    <form action="{% url 'book' flight.id %}" method="post">
        <select name="passenger">
            {% for passenger in non_passengers %}
                <option value="{{ passenger.id }}">{{ passenger }}</option>
            {% endfor %}
        </select>
        <input type="submit" value="Book flight" />
    </form>
{% else %}
    <div>No passengers to add.</div>
{% endif %}

(flights/admin.py) 
from .models import Passenger
admin.site.register(Passenger)

# CROSS-SITE REQUEST FORGERY:
add {% csrf_token %} in the form 
<form action="{% url 'book' flight.id %} method="post">
    {% csrf_token %}
    <select name="passenger">

# MODIFYING ADMIN:
(flights/admin.py)
class PassengerInline(admin.StackedInline):
    model = Passenger.flights.through
    extra = 1

class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInline]

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights")

admin.site.register(Passenger, PassengerAdmin)

# STATIC FILES:
flights/static/flights/styles.css
{% load static %} at the top of the html file
<link rel="stylesheet" href="{% static 'flights/styles.css' %}"/>

# LOGIN AND AUTHENTICATION:
viewing the authentication app:

> from django.contrib.auth.models import User
> u = User(first="Juan", last="Perez") ????

python manage.py runserver

the __init__.py inside the directory means: this is a python package.

