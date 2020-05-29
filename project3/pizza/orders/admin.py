from django.contrib import admin
from .models import Size, PizzaType, ToppingsType, Pizza, Topping, Order

# Register your models here.

# this group of classe adds funtionality in the Topping page
class PizzaInline(admin.StackedInline):
    model = Pizza.toppings.through
    extra = 1

class ToppingAdmin(admin.ModelAdmin):
    inlines = [PizzaInline]

# this class adds funtionality in the Pizza page
class PizzaAdmin(admin.ModelAdmin):
    filter_horizontal = ("toppings",) # don't forget the comma!! 

class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ("pizzas",) # don't forget the comma!! 

admin.site.register(Size)
admin.site.register(PizzaType)
admin.site.register(ToppingsType)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Order, OrderAdmin)