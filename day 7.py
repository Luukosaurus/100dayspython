import random
wordlist = ["appel","kaas","boom"]
lives = 6
woord = random.choice(wordlist)
print(woord)
inviswoord = []
done = False
for i in range(len(woord)):
    inviswoord += "_"
while not done:
    userinput = input("Kies een letter\n")
    lastlocation = 0
    if userinput in woord:
        for i in range(woord.count(userinput)):
            location = woord.index(userinput,lastlocation)
            lastlocation = location+1
            inviswoord[location] = userinput
            print("test")
    else:
        lives -= 1
        if lives <= 0:
            print("Your dead")
            exit()
    print(''.join(inviswoord))
    print(f"You have {lives} left.")
