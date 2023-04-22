from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.score = 0
        self.level_up()

    def level_up(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='left', font=FONT)
        self.score += 1

    def call_end(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", move=False, align='center', font=FONT)