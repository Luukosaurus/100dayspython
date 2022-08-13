# Copy paste this in https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

while not at_goal():
    def turn_right():
        turn_left()
        turn_left()
        turn_left()
    def turn_back():
        turn_left()
        turn_left()
    if right_is_clear():
        turn_right()
        move()
    else:
        turn_left()