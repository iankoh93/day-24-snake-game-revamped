from turtle import Turtle
STEPS = 20
NORTH = 90
EAST = 0
WEST = 180
SOUTH = 270


class Snake(Turtle):
    def __init__(self, starting_length=3):
        super().__init__()
        self.snakeBody = []
        for i in range(0, starting_length):
            self.add_segment((0, 0))
            self.snakeBody[i].setpos(x=i * -20, y=0)

    def move(self):
        for body in range(len(self.snakeBody) - 1, 0, -1):
            new_x = self.snakeBody[body - 1].xcor()
            new_y = self.snakeBody[body - 1].ycor()
            self.snakeBody[body].goto(new_x, new_y)
        self.snakeBody[0].forward(STEPS)

    def add_segment(self, position):
        # Add new segment to the snake
        new_body = Turtle()
        new_body.shape("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(position)
        self.snakeBody.append(new_body)

    def extend(self):
        self.add_segment(self.snakeBody[-1].position())

    def up(self):
        if self.snakeBody[0].heading() != SOUTH:
            self.snakeBody[0].setheading(NORTH)

    def down(self):
        if self.snakeBody[0].heading() != NORTH:
            self.snakeBody[0].setheading(SOUTH)

    def east(self):
        if self.snakeBody[0].heading() != WEST:
            self.snakeBody[0].setheading(EAST)

    def west(self):
        if self.snakeBody[0].heading() != EAST:
            self.snakeBody[0].setheading(WEST)
