from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.showturtle()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def check_where(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

    def go_to_start(self):
        self.goto(STARTING_POSITION)
