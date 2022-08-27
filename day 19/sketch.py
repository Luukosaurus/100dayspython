import turtle
class drawing():
    screen = turtle.Screen()
    turtle.pensize(1)
    def forward():
        turtle.forward(5)
    def backward():
        turtle.back(5)
    def left():
        turtle.left(4)
    def right():
        turtle.right(4)
    def clear():
        pos = turtle.pos()
        heading = turtle.heading()
        turtle.resetscreen()
        turtle.speed(10)
        turtle.penup()
        turtle.goto(pos)
        turtle.pendown()
        turtle.setheading(heading)
        turtle.speed(3)
    screen.listen()
    screen.onkeypress(forward, "w")
    screen.onkeypress(backward, "s")
    screen.onkeypress(left, "a")
    screen.onkeypress(right, "d")
    screen.onkey(clear,"c")
    screen.exitonclick()