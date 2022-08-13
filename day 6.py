# Copy paste this in https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_back():
    turn_left()
    turn_left()
if front_is_clear():
    while front_is_clear():
        move()
        if is_facing_north():
            break
        else:
            turn_left()
else:
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
