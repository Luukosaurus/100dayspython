from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#Below this is my code
KoffieMagine = CoffeeMaker()
KoffieMenu = Menu()
GeldMagine = MoneyMachine()
done = False
def buy_coffee(coffee):
    if KoffieMenu.find_drink(coffee) == None: return
    if KoffieMagine.is_resource_sufficient(KoffieMenu.find_drink(coffee)):
        if GeldMagine.make_payment(KoffieMenu.find_drink(coffee).cost):
            KoffieMagine.make_coffee(KoffieMenu.find_drink(coffee))
while not done:
    todo = input("Wat wil je (espresso/latte/cappuccino)\n")
    if todo == "report":
        KoffieMagine.report()
        GeldMagine.report()
        input("Continue")
    elif todo == "off":
        print("Turning off")
        done = True
    else:
        buy_coffee(todo)
        input("Continue")