from django.db import models

# Create your models here.

class Size(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class PizzaType(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class ToppingsType(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class Topping(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class Pizza(models.Model):
    isModel = models.BooleanField(default=False)
    pizzaType = models.ForeignKey(PizzaType, on_delete=models.CASCADE, related_name="pizzas")
    toppingsType = models.ForeignKey(ToppingsType, on_delete=models.CASCADE, related_name="pizzas")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="pizzas")   
    toppings = models.ManyToManyField(Topping, blank=True, related_name="pizzas")  #, max_length = 5)
    price = models.FloatField()

    def __str__(self):
        # print (self.toppings)
    
        modelText = ""
        
        if self.isModel == True:
            modelText = "model:"
        
        priceText = "{:.2f}"
        priceText = priceText.format(self.price)
        toppingsText = ""
        topps = self.toppings.all()
        for topp in topps:
            toppingsText += " " + topp.name
        return modelText + f"{self.pizzaType} pizza - {self.toppingsType} - {self.size} - {toppingsText}: {priceText} $" 

class Order(models.Model):
    client = models.CharField(max_length=64)
    pizzas = models.ManyToManyField(Pizza, blank=True, related_name="in_order")
    # subs
    # salads
    # pasta
    # dinner dishes
    totalPrice = models.FloatField()

    def __str__(self):
        print(self.client)
        print(self.pizzas)
        print(self.totalPrice)
        return f"Order from {self.client}: {self.totalPrice}"

