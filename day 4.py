import random
randomnr = random.randint(1,3)
userinput = input("Rock(1) Paper(2) Scissors(3)\n")
if userinput == "1" or userinput == "rock" or userinput == "Rock" or userinput == "steen" or userinput == "Steen":
    print("you chose Rock")
    if randomnr == 1:
        print("The computer chose Rock")
        print("You had a draw")
    elif randomnr == 2:
        print("The computer chose Paper")
        print("You lost")
    elif randomnr == 3:
        print("The computer chose Scissors")
        print("You won")
    else:
        print("Error: Random input not valid")
elif userinput == "2" or userinput == "paper" or userinput == "Paper" or userinput == "papier" or userinput == "Papier":
    print("you chose Paper")
    if randomnr == 1:
        print("The computer chose Rock")
        print("You won")
    elif randomnr == 2:
        print("The computer chose Paper")
        print("You had a draw")
    elif randomnr == 3:
        print("The computer chose Scissors")
        print("You lost")
    else:
        print("Error: Random input not valid")
elif userinput == "3" or userinput == "scissors" or userinput == "=Scissors" or userinput == "schaar" or userinput == "Schaar":
    print("you chose Scissors")
    if randomnr == 1:
        print("The computer chose Rock")
        print("You lost")
    elif randomnr == 2:
        print("The computer chose Paper")
        print("You won")
    elif randomnr == 3:
        print("The computer chose Scissors")
        print("You had a draw")
    else:
        print("Error: Random input not valid")
else:
    print("invalid input try again")
