import random
print("Password generator")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
customtekens = "!@#$%^&*()<>?:'{}_+,./;[]-="
wachtwoord = ""
customstr = input("Wil je een custom wachtwoord of helemaal random. \nType 'custom' of 'random'\n")
if(customstr == "custom"):
    letters = int(input("hoeveel letters wil je in je wachtwoord\n"))
    cijfers = int(input("hoeveel cijfers wil je in je wachtwoord\n"))
    tekens = int(input("hoeveel symbolen wil je in je wachtwoord\n"))
    all = letters+cijfers+tekens
    total = all
    for i  in range(all):
        teken = random.randint(0,total-1)
        if(0 <= teken <letters):
            wachtwoord += alphabet[random.randint(0,25)]
            letters -= 1
            total -= 1
        elif(letters <= teken <cijfers+letters):
            wachtwoord += str(random.randint(0,9))
            cijfers -= 1
            total -= 1
        elif(cijfers+letters <= teken <tekens+cijfers+letters):
            wachtwoord += customtekens[random.randint(0,9)]
            tekens -= 1
            total -= 1
    print(wachtwoord)
elif(customstr == "random"):
    all = int(input("Hoelang wil je je wachtwoord hebben\n"))
    for i  in range(all):
        welkteken = random.randint(1,3)
        if(welkteken == 1):
            wachtwoord += alphabet[random.randint(0,25)]
        elif(welkteken == 2):
            wachtwoord += str(random.randint(0,9))
        elif(welkteken == 3):
            wachtwoord += customtekens[random.randint(0,26)]
    print(wachtwoord)
else:
    print("Foute input")