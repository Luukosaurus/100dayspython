import random
nummer = random.randint(1,100)
done = False
moeilijkhijd = input("Wil je makkelijk of moeilijk\n")
if moeilijkhijd in "makkelijk":
    levens = 10
elif moeilijkhijd in "moeilijk":
    levens = 5
else:
    print("Fout")
    exit()
while not done:
    keuze = int(input("Maak een gok "))
    if keuze == nummer:
        print("Je hebt gewonnen")
        done = True
        print(f"Je hebt nog {levens} levens.")
    elif keuze > nummer:
        print("Je gok was te hoog")
        levens -= 1
        print(f"Je hebt nog {levens} levens.")
    elif keuze < nummer:
        print("Je gok was te laag")
        levens -= 1
        print(f"Je hebt nog {levens} levens.")
    if levens <= 0:
        print("je bent af")
        exit()
