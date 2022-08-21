import random
alles = {"Erik": 2000,"Sven": 2,"Ole":788,"Luuk": 99999999999999999999999}
alleslist = list(alles.items())
done = False
score = 0
randomint1 = random.randint(0,3)
while not done:
    diferent = False
    while not diferent:
        randomint2 = random.randint(0,3)
        if randomint1 != randomint2:
            diferent = True
    userinput = input(f"{alleslist[randomint1][0]} Heeft een score van {alleslist[randomint1][1]}. \nIs de score van {alleslist[randomint2][0]} hoger of lager?\n")
    if userinput in "hoger":
        hogerkeuze = True
    elif userinput in "lager":
        hogerkeuze = False
    if alleslist[randomint1][1] < alleslist[randomint2][1]:
        hogerfijt = True
    else:
        hogerfijt = False
    if hogerfijt == hogerkeuze:
        score += 1
        print(f"Goed gedaan je score is nu {score}")
        randomint1 = randomint2
    else:
        print(f"Jij noob je bent af je score was {score}")
        done = True
