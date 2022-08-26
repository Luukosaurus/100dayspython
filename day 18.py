import turtle
import random
turtle.dot(10)
turtle.speed(10000)
turtle.penup()
turtle.colormode(255)
turtle.goto(-460,-380)
turtle.hideturtle()
left = True
for i in range(39):
    for i in range(47):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        turtle.color((r,g,b), (r,g,b))
        turtle.dot(15)
        turtle.forward(20)
    if left:
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        left = False
    else:
        turtle.left(-90)
        turtle.forward(20)
        turtle.left(-90)
        turtle.forward(20)
        left = True
turtle.done()