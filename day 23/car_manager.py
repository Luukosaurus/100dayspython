import turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 1
STARTING_AVERAGE_CARS = 20

class CarManager:
    speed = STARTING_MOVE_DISTANCE
    averagecars = 0
    spawnchance = 0
    carlist = []
    def __init__(self,screen):
        screen.register_shape("car",((-15,10),(15,10),(15,-10),(-15,-10)))
        self.makediffeculty(1)
    def makediffeculty(self,level):
        self.speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT*level
        self.averagecars = STARTING_AVERAGE_CARS - 1 + level
        self.spawnchance = round(650/self.speed/self.averagecars)
    def createcar(self):
        if random.randint(0,self.spawnchance) == 0:
            carseed = random.randint(0,5)
            carturtle = turtle.Turtle("car")
            carturtle.color(COLORS[carseed])
            carturtle.penup()
            carturtle.speed(0)
            carturtle.goto(320,random.randint(-240,280))
            self.carlist.append(carturtle)
    def movecars(self):
        for car in self.carlist:
            car.setx(car.xcor()-self.speed)
    def deletecars(self):
        for car in self.carlist:
            if car.xcor() <= -350:
                self.carlist.remove(car)
                car.hideturtle()
    def checkplayer(self,player):
        for car in self.carlist:
            if car.xcor()+20 > player.xcor()and car.xcor()-20 < player.xcor() and car.ycor()+20 > player.ycor()and car.ycor()-20 < player.ycor():
                return True


