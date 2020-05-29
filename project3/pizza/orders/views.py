from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Size, PizzaType, ToppingsType, Pizza, Topping, Order
import json

# Create your views here.

orderCreated = False
myOrder = ""

def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    return HttpResponseRedirect(reverse("menu"))

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username= username, password= password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def menu(request):
    global orderCreated   
    if orderCreated:
        pizzas = myOrder.pizzas.all()
        total = myOrder.totalPrice
    else:
        pizzas = []
        total = 0

    context = { 
        "user": request.user,
        "pizzaTypes": PizzaType.objects.all(),
        "sizes": Size.objects.all(),
        "toppingsTypes": ToppingsType.objects.all(),
        "toppings": Topping.objects.all(),
        "pizzas" : pizzas,
        "total": total
    }
    return render(request, "orders/menu.html", context) 

def add_item(request):
    try: 
        pizzaTypeID = request.POST["pizzaType"]
        sizeID = request.POST["size"]
        toppingsTypeID = request.POST["toppingsType"]    
        topping1ID = request.POST["topping1"]    
        topping2ID = request.POST["topping2"]
        topping3ID = request.POST["topping3"]

        pizzaType = PizzaType.objects.get(id=pizzaTypeID)
        size = Size.objects.get(id=sizeID)
        toppingsType = ToppingsType.objects.get(id=toppingsTypeID)
        topping1 = Topping.objects.get(id=topping1ID)    
        topping2 = Topping.objects.get(id=topping2ID)
        topping3 = Topping.objects.get(id=topping3ID)       
    
        modelPizza = Pizza.objects.get(isModel=True, pizzaType=pizzaType, size=size, toppingsType=toppingsType)
    except KeyError:
        return render(request, "orders/error.html", {"message": "no item selected"})
    except Pizza.DoesNotExist:
        return render(request, "orders/error.html", {"message": "That combination is not valid - please select again"})

    global orderCreated 
    global myOrder
    if orderCreated is False: # only the first time
        userName = str(request.user)
        myOrder = Order(client=userName, totalPrice=0)
        myOrder.save()
        orderCreated = True

    customPizza = Pizza(pizzaType=pizzaType, size=size, toppingsType=toppingsType, price = modelPizza.price) 
    customPizza.save()

    if toppingsType.name == "1 topping":
        customPizza.toppings.add(topping1)

    if toppingsType.name == "2 toppings":
        customPizza.toppings.add(topping1)
        customPizza.toppings.add(topping2)

    if toppingsType.name == "3 toppings":
        customPizza.toppings.add(topping1)
        customPizza.toppings.add(topping2)
        customPizza.toppings.add(topping3)
    
    myOrder.pizzas.add(customPizza)
    myOrder.totalPrice += customPizza.price
    myOrder.totalPrice = round(myOrder.totalPrice,2)
    myOrder.save()

    return HttpResponseRedirect(reverse("menu")) 

def confirm_order(request):
    # message = request.POST["message"] # using an ajax request
    # print (message)
    # answer = {"success": True}
    # return json.dumps(answer)
    global orderCreated
    orderCreated = False
    context = { 
        "user": request.user,
        "order": myOrder,
        "pizzas": myOrder.pizzas.all()
    }
    return render(request, "orders/order.html", context) 

    # return render(request, "orders/success.html", {"title": "Thank you.", "message": "Your order has been placed."})
