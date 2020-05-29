# Project 3

Web Programming with Python and JavaScript

# First steps:
cd C:\Users\spa3cap\Documents\GitHub\django (0)
py -3 -m venv venv (install virtual enviroment)
venv\Scripts\activate (activate) (1)
python -m pip install --upgrade pip (update pip)
pip install Django==3.0.6
pip3 install -r requirements.txt
cd c:\Users\spa3cap\Documents\Github\project3\pizza (2)
django-admin startproject pizza (creates the project)
cd pizza
python manage.py startapp orders (creates the app)

# (orders/urls.py - create)
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index")
]

# (orders/views.py)
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("Project 3: TODO")

# (pizza/urls.py)
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path("", include("orders.urls")),
    path("admin/", admin.site.urls),
]

# (pizza/setings.py)
INSTALLED_APPS = [
    'orders.apps.OrdersConfig',
    'django.contrib.admin',

 # (shell) 
 > python manage.py runserver   

# (orders/models.py)
class Topping(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

# (shell)
> from orders.models import Topping
> t = Topping (name="Pepperoni")
> t.save()
> Topping.objects.all()

# (orders/admin.py)
from .models import Topping
admin.site.register(Topping)
> python manage.py createsuperuser
> user: spa3cap
> pass: Bambilandia
run the server and then access the admin route

# rendering html example

# html inheritance

# start again with the models
erase the db.sqlite3
erase the migrations files
> python manage.py createsuperuser

# cross-site request forgery:
add {% csrf_token %} inside the form:
<form...>
   {% csrf_token %}
   <select ...> ...

# managin models (done)

# add static files (done)
add css file (done)
add js file (done)

# users administration (done)
(shell)
> from django.contrib.auth.models import User
> user = User.objects.create_user(username="alice", email="alice@something.com", password="alice12345")
user.first_name = "Alice"
user.last_name = "Appleseed"
user.save()

# variable route (...)

# create an ajax request (...)
    <p> 
        <button id="addItem" class="w3-btn w3-red"> add item </button>
    </p>







