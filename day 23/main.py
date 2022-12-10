import time
from turtle import Screen,done
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

level = 1
moving = False
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
carmanager = CarManager(screen)
game_is_on = True

screen.listen()
screen.onkeypress(player.move, "w")
screen.onkey(player.dontmove,"w")
scoreboard = Scoreboard()
while game_is_on:
    timer = time.time()
    wait = 0.02
    while timer + wait > time.time():
      pass
    carmanager.createcar()
    carmanager.movecars()
    carmanager.deletecars()
    player.updatelocation()
    if player.turtle.ycor() > 290:
        level += 1
        player.gotostart()
        carmanager.makediffeculty(level)
    if carmanager.checkplayer(player.turtle):
        game_is_on = False
        scoreboard.gameover()
    scoreboard.update(level)
    screen.update()
done()