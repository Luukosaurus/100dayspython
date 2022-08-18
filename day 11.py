import random
import os 
playing = True
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
while playing:
    userdone = False
    computerdone = False
    usercardlist = []
    computercardslist = []
    usercardlist.append(random.choice(cards))
    usercardlist.append(random.choice(cards))
    computercardslist.append(random.choice(cards))
    computercardslist.append(random.choice(cards))
    potje = True
    while potje:
        os.system('cls')
        if not userdone:
            print(f"Jou kaarten zijn {usercardlist}")
            print(f"De eerste kaart van de computer is {computercardslist[0]}")
            nogeen = input("Wil je nog een kaart krijgen ja of nee ")
            if nogeen in "ja":
                usercardlist.append(random.choice(cards))
            else:
                userdone = True
        if sum(computercardslist) < 14:
            computercardslist.append(random.choice(cards))
        else:
            computerdone = True
        if computerdone and userdone:
            potje = False
        if sum(usercardlist) > 21:
            potje = False
    os.system('cls')
    print(f"Jouw kaarten zijn {usercardlist}")
    print(f"De kaarten van de computer zijn {computercardslist}")
    if sum(usercardlist) < 21:
        if sum(computercardslist) < 21:
            if sum(usercardlist) > sum(computercardslist):
                print("You win")
            elif sum(usercardlist) == sum(computercardslist):
                print("Its a draw")
            else:
                print("You lost")
        else:
            print("You win")
    else:
        print("You lost")
    nogeenkeer = input("Wil je nog een keer ja of nee\n")
    if nogeen in "nee":
        playing = False
