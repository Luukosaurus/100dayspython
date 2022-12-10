FONT = ("Courier", 24, "normal")
import turtle

class Scoreboard:
    def __init__(self):
        self.score = turtle.Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(-220,250)
        self.score.write("score: 1", False, "center" , FONT)
    def update(self,level):
        self.score.clear()
        self.score.write("score: "+ str(level),False, "center", FONT)
    def gameover(self):
        self.mid = turtle.Turtle()
        self.mid.hideturtle()
        self.mid.penup()
        self.mid.goto(0,0)
        self.mid.write("GAME OVER",False, "center", FONT)
