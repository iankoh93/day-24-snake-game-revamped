from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Comic Sans", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.high_score = int(self.open_score())
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(x=0, y=270)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.current_score}   High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.current_score}")
        self.current_score = 0
        self.print_score()

    def open_score(self):
        with open("highscore.txt", mode="r") as file:
            score = file.read()
            return score
