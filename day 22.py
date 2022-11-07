import datetime
import turtle
import random
import time
scale = 0.8
screen = turtle.Screen()
screen.bgcolor("black")
screen.register_shape("padle",((-10*scale,60*scale),(10*scale,60*scale),(10*scale,-60*scale),(-10*scale,-60*scale)))
turtle.mode("logo")
turtle.delay(0)
class player():
    going = [0,0]
    speed = 5
    bounds = 440*scale,340*scale
    def __init__(self,number):
        self.player = turtle.Turtle("padle")
        self.player.penup()
        self.player.color("white")
        if number == 1:
            self.player.goto(-400*scale,0)
        elif number == 2:
            self.player.goto(400*scale,0)
    def up(self):
        self.going = [self.going[0],1*self.speed*scale]
    def down(self):
        self.going = [self.going[0],-1*self.speed*scale]
    def left(self):
        self.going = [-1*self.speed*scale,self.going[1]]
    def right(self):
        self.going = [1*self.speed*scale,self.going[1]]
    def release(self):
        self.going = [0,0]
    def updateplayer(self):
        self.player.goto(self.player.pos()+(self.going))
        if self.player.pos()[1] > self.bounds[1]:
            self.player.goto(self.player.pos()[0],self.bounds[1])
        if self.player.pos()[1] < -self.bounds[1]:
            self.player.goto(self.player.pos()[0],-self.bounds[1])
        if self.player.pos()[0] > self.bounds[0]:
            self.player.goto(self.bounds[0],self.player.pos()[1])
        if self.player.pos()[0] < -self.bounds[0]:
            self.player.goto(-self.bounds[0],self.player.pos()[1])
class map():
    mapmaker = turtle.Turtle()
    def makemap(self):
        self.mapmaker.hideturtle()
        self.mapmaker.color("white")
        self.mapmaker.penup()
        self.makemiddleline()
        self.makeouterbox()
    def makemiddleline(self):
        self.mapmaker.penup()
        self.mapmaker.goto(0,400*scale)
        self.mapmaker.right(180)
        self.mapmaker.pensize(3*scale)
        for i in range(20):
            self.mapmaker.pendown()
            self.mapmaker.forward(20*scale)
            self.mapmaker.penup()
            self.mapmaker.forward(20*scale)
    def makeouterbox(self):
        self.mapmaker.penup()
        self.mapmaker.pensize(1)
        self.mapmaker.goto(-450*scale,400*scale)
        self.mapmaker.pendown()
        self.mapmaker.goto(450*scale,400*scale)
        self.mapmaker.goto(450*scale,-400*scale)
        self.mapmaker.goto(-450*scale,-400*scale)
        self.mapmaker.goto(-450*scale,400*scale)
class ball():
    speed = 2
    pongball = turtle.Turtle("circle")
    def __init__(self,player1,player2):
        self.pongball.color("white")
        self.pongball.penup()
        self.pongball.shapesize(scale)
        self.pongball.setheading(-99)
        self.player1 = player1
        self.player2 = player2
    def move(self):
        self.pongball.forward(self.speed)
    def collisioncheck(self):
        def checkupanddown():
            if self.pongball.pos()[1] >390*scale:
                if 90 > self.pongball.heading() > 0:
                    self.pongball.setheading(180-self.pongball.heading())
                elif 360 > self.pongball.heading() > 270:
                    self.pongball.setheading(180 + (360-self.pongball.heading()))
            elif self.pongball.pos()[1] < -390*scale:
                if 180 > self.pongball.heading() > 90:
                    self.pongball.setheading(180-self.pongball.heading())
                elif 270 > self.pongball.heading() > 180:
                    self.pongball.setheading(180-self.pongball.heading())
        def checkbackwalls():
            if self.pongball.pos()[0] >440*scale:
                self.pongball.goto(0,0)
                time.sleep(3)
            elif self.pongball.pos()[0] < -440*scale:
                self.pongball.goto(0,0)
                time.sleep(3)
        def checkplayers():
            #Fix angle calculations
            if self.player2.position()[0]+10*scale > self.pongball.pos()[0] > self.player2.position()[0]-10*scale:
                if self.player2.position()[1] +70*scale> self.pongball.pos()[1] > self.player2.position()[1]-70*scale:
                    if self.pongball.heading() <180:
                        angle =  self.pongball.pos()[1] - self.player2.pos()[1]
                        angle += 270
                        self.pongball.setheading(angle)
            if self.player1.position()[0]+10*scale > self.pongball.pos()[0] > self.player1.position()[0]-10*scale:
                if self.player1.position()[1] +70*scale> self.pongball.pos()[1] > self.player1.position()[1]-70*scale:
                    if self.pongball.heading() >180:
                        angle =  self.player1.pos()[1] - self.pongball.pos()[1]
                        angle += 90
                        self.pongball.setheading(angle)
        checkupanddown()
        checkbackwalls()
        checkplayers()
player1 = player(1)
player2 = player(2)
#Dit is niet clean
player_1 = player1.player
player_2 = player2.player
map = map()
map.makemap()
ball = ball(player_1,player_2)
screen.listen()
screen.onkeypress(player1.up, "w")
screen.onkeypress(player1.down, "s")
screen.onkey(player1.release, "w")
screen.onkey(player1.release, "s")
screen.onkeypress(player2.up, "Up")
screen.onkeypress(player2.down, "Down")
screen.onkey(player2.release, "Up")
screen.onkey(player2.release, "Down")
screen.onkeypress(player1.left, "a")
screen.onkeypress(player1.right, "d")
screen.onkey(player1.release, "a")
screen.onkey(player1.release, "d")
screen.onkeypress(player2.left, "Left")
screen.onkeypress(player2.right, "Right")
screen.onkey(player2.release, "Left")
screen.onkey(player2.release, "Right")
for i in range(1000000):
    ball.move()
    ball.collisioncheck()
    player1.updateplayer()
    player2.updateplayer()
    timer = time.time()
    wait = 0.005
    while timer + wait > time.time():
      pass
turtle.done()