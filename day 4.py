import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

randomnr = random.randint(0,2)
asciiimage = [rock,paper,scissors]
namenrs = ["Rock","Paper","Scissors"]
userinput = int(input("Rock(1) Paper(2) Scissors(3)\n")) -1
if(userinput >2 or userinput < 0):
    print("Wrong input try again")
    exit()
print(f"You chose {namenrs[userinput]}")
print(asciiimage[userinput])
print(f"The computer chose {namenrs[randomnr]}")
print(asciiimage[randomnr])
if(userinput == randomnr):
    print("It's a draw")
elif(userinput - randomnr == -1 or userinput - randomnr == 2):
    print("You lost")
elif(userinput - randomnr == 1 or userinput - randomnr == -2):
    print("You won")
else:
    print(f"Something went wrong you chose {userinput} the computer chose {randomnr}")
