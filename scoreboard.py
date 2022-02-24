from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Comic Sans", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(x=-20, y=270)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score:  {self.current_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", move=False, align=ALIGNMENT, font=FONT)