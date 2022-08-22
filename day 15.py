import os
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
done = False
def askmoney(coffee,current,cost):
    print(f"Je hebt nog niet genoeg muntjes betaald. Je hebt {round(current, 2)} betaald en het kost {cost}")
    kwartjes = int(input("Hoeveel kwartjes wil je geven(25c) "))
    dubbeljes = int(input("Hoeveel dubbeljes wil je geven(10c) "))
    stuivers = int(input("Hoeveel stuivers wil je geven(5c) "))
    centen = int(input("Hoeveel centen wil je geven(1c) "))
    betaald = kwartjes * 0.25 + dubbeljes * 0.10 + stuivers * 0.05 + centen * 0.01
    return betaald
def printreport():
    print(f"Er is nog\n{resources['water']} ml water\n{resources['milk']} ml melk\n{resources['coffee']} gram koffie")
def checkresources(nodig):
    if "water" in nodig:
        if nodig["water"] > resources["water"]:
            print("Niet genoeg water.")
            return False
    if "milk" in nodig:
        if nodig["milk"] > resources["milk"]:
            print("Niet genoeg melk.")
            return False
    if "coffee" in nodig:
        if nodig["coffee"] > resources["coffee"]:
            print("Niet genoeg koffie.")
            return False
    return True
def takeresources(nodig):
    if "water" in nodig:
        resources["water"] -= nodig["water"]
    if "milk" in nodig:
        resources["milk"] -= nodig["milk"]
    if "coffee" in nodig:
        resources["coffee"] -= nodig["coffee"]
while not done:
    os.system('cls')
    betaald = 0
    todo = input("Wat wil je (espresso/latte/cappuccino)\n")
    if todo in "espresso":
        cost = MENU["espresso"]["cost"]
        while betaald < MENU["espresso"]["cost"]:
            betaald += askmoney("espresso",betaald,cost)
        over = betaald - cost
        nodig = MENU["espresso"]["ingredients"]
        if checkresources(nodig):
            takeresources(nodig)
            print(f"Hier is je koffie en je wisselgeld({round(over,2)})")
        else:
            print(f"Je hebt je {round(betaald)} in cash terug gekregen")
    elif todo in "latte":
        cost = MENU["latte"]["cost"]
        while betaald < cost:
            betaald += askmoney("latte",betaald,cost)
        over = betaald - cost
        nodig = MENU["latte"]["ingredients"]
        if checkresources(nodig):
            takeresources(nodig)
            print(f"Hier is je koffie en je wisselgeld({round(over,2)})")
        else:
            print(f"Je hebt je {round(betaald)} in cash terug gekregen")
    elif todo in "cappuccino":
        cost = MENU["cappuccino"]["cost"]
        while betaald < cost:
            betaald += askmoney("cappuccino",betaald,cost)
        over = betaald - cost
        nodig = MENU["latte"]["ingredients"]
        if checkresources(nodig):
            takeresources(nodig)
            print(f"Hier is je koffie en je wisselgeld({round(over,2)})")
        else:
            print(f"Je hebt je {round(betaald)} in cash terug gekregen")
    elif todo in "report":
        printreport()
    elif todo in "off":
        done = True
        print("turning off")
    input("Druk op enter om verder te gaan")