import turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 2
FINISH_LINE_Y = 280
turtle.mode("logo")
turtle.delay(0)
class Player:
    moving = False
    def __init__(self):
        Player.createplayer(self)
        Player.gotostart(self)
    def createplayer(self):
        self.turtle = turtle.Turtle("turtle")
        self.turtle.penup()
    def gotostart(self):
        self.turtle.goto(STARTING_POSITION)
    def move(self):
        self.moving = True
    def dontmove(self):
        self.moving = False
    def updatelocation(self):
        if self.moving:
            self.turtle.sety(self.turtle.ycor()+MOVE_DISTANCE)