done = False
def plus(getal1, getal2):
    uitkomst = getal1 + getal2
    return uitkomst
def minus(getal1, getal2):
    uitkomst = getal1 - getal2
    return uitkomst
def keer(getal1, getal2):
    uitkomst = getal1 * getal2
    return uitkomst
def delendoor(getal1, getal2):
    uitkomst = getal1 / getal2
    return uitkomst
def printer(getal1, getal2,teken,uitkomst):
    print(str(getal1) + teken + str(getal2) + " = " + str(uitkomst))
while not done:
    first = float(input("Wat is je eerste getal\n"))
    finished = False
    while not finished:
        Teken = input('Welke functie wil je gebruiken "+", "-", "*" of "/"\n')
        second = float(input("Wat is je tweede getal\n"))
        if Teken == "+":
            uitkomst = plus(first,second)
            printer(first,second,Teken,uitkomst)
        elif Teken == "-":
            uitkomst = minus(first,second)
            printer(first,second,Teken,uitkomst)
        elif Teken == "*":
            uitkomst = keer(first,second)
            printer(first,second,Teken,uitkomst)
        elif Teken == "/":
            uitkomst = delendoor(first,second)
            printer(first,second,Teken,uitkomst)
        else:
            exit()
        verder = input("Wil je verder rekenen met dit getal ja of nee\n")
        if verder in "ja":
            first = uitkomst
        else:
            finished = True
    stoppen = input("Wil je stoppen met berekeningen maken ja of nee\n")
    if stoppen in "ja":
        done = True