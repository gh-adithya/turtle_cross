from turtle import Turtle
import random
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_instances = []
        self.initial_speed = STARTING_MOVE_DISTANCE
        self.speed_boost = MOVE_INCREMENT
        self.level = 0

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_car = Turtle("square")
            new_car.hideturtle()
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            y_cordi = random.randint(-270, 270)
            new_car.goto(300, y_cordi)
            new_car.showturtle()
            self.car_instances.append(new_car)

    def inc_speed(self):
        """ Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a
         successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed
         in the centre. If you get stuck, check the video walkthrough in Step 7."""
        self.initial_speed += self.speed_boost
        self.level += 1

    def move_cars(self):
        for car in self.car_instances:
            car.forward(self.initial_speed)



