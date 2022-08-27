import turtle
import random
colors = ["red","blue","green","yellow","pink"]
players = []
class Race:
    def __init__(self):
        Race.draw_map()
        Race.Addplayers(5)
        bet = Race.GetBet()
        winner = Race.StartRace(self,players)
        Race.GiveResults(winner,bet)
        turtle.done()
    def draw_map():
        mapturtle = turtle.Turtle()
        mapturtle.hideturtle()
        mapturtle.penup() 
        mapturtle.goto(-450,-400)
        mapturtle.left(90)
        mapturtle.pendown()
        mapturtle.forward(800)
        mapturtle.penup()
        mapturtle.speed(10)
        mapturtle.goto(450,-400)
        mapturtle.speed(3)
        mapturtle.pendown()
        mapturtle.forward(800)
    def Addplayers(amount):
        for i in range(amount):
            player = turtle.Turtle()
            player.color(colors[i])
            player.shape("turtle")
            player.penup() 
            player.goto(-470,-200 + 100*i)
            player.speed(8)
            players.append(player)
    def GetBet():
        bet = input("choose a color ")
        while bet not in colors:
            bet = input("That is not a valid color try again ")
        return bet
    def StartRace(self,players):
        done = False
        while not done:
            for player in players:
                player.forward(random.randint(0,5))
                if player.xcor() > 455:
                    winningcolor = player.color()[0]
                    done = True
        return winningcolor
    def GiveResults(winner,bet):
        if winner == bet:
            print(f"You won with the color {bet}")
        else:
            print(f"You lost with the color {bet} the winner was {winner}")

