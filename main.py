import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(tim.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.car_instances:
        if car.distance(tim) < 20:
            scoreboard.call_end()
            game_is_on = False
    if tim.check_where():
        scoreboard.level_up()
        car_manager.inc_speed()
        tim.go_to_start()


screen.exitonclick()