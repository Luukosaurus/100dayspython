import random
import time
import turtle
SnakeParts = []
screen = turtle.Screen()
head = turtle.Turtle("square")
head.color("red")
head.penup()
head.speed(10)
apple = turtle.Turtle("circle")
apple.color("red")
apple.penup()
apple.speed(10)
SnakeParts.append(head)
color = 0
turtle.colormode(255)
turtle.delay(0)
done = False
def MakeSnake():
    for i in range(4):
        SnakePart = turtle.Turtle("square")
        SnakePart.penup()
        SnakePart.speed(10)
        SnakeParts.append(SnakePart)
def checkapple():
    if str(head.pos()) == str(apple.pos()):
        SnakePart = turtle.Turtle("square")
        SnakePart.penup()
        SnakePart.speed(10)
        SnakeParts.append(SnakePart)
        newx = random.randint(0,23)
        newy = random.randint(0,20)
        apple.goto(newx*20,newy*20)
    else:
        print(str(head.pos()) + " : " + str(apple.pos()))
def checkzelf():
    for part in SnakeParts:
        if str(part.pos()) == str(head.pos()):
            if part is not head:
                print("Your dead you noob")
                print(f"Your score is {len(SnakeParts) - 6}")
                return True
def Move():
    reverse = list(reversed(SnakeParts))
    for part in reverse:
        if 'oldpart' in locals():
            oldpart.goto(part.pos())
        oldpart = part
    SnakeParts[0].forward(20)
    checkapple()
    if checkzelf():
        return True
def up():
    if head.heading() == 270.0:
        pass
    else:
        head.seth(90)
def down():
    if head.heading() == 90.0:
        pass
    else:
        head.seth(270)
def left():
    if head.heading() == 0.0:
        pass
    else:
        head.seth(180)
def right():
    if head.heading() == 180.0:
        pass
    else:
        head.seth(0)
MakeSnake()
checkapple()
screen.listen()
screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")
while not done:
    time.sleep(0.1)
    done = Move()
screen.exitonclick()
            
            


