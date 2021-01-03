import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()

screen.onkey(player.move_forward, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Update score board if player cross the finish line
    if player.ycor() > 280:
        scoreboard.add_score()

    # Check if player react the finish line
    player.back_to_begining()



screen.exitonclick()