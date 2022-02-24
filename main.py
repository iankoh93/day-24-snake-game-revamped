from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up the game screen
LIMITS = 300
screen = Screen()
screen.setup(width=LIMITS*2, height=LIMITS*2)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)
game_is_on = True

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.west, key="Left")
screen.onkey(fun=snake.east, key="Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check if there was a collision with food
    if snake.snakeBody[0].distance(food) < 20:
        food.refresh()
        snake.extend()
        score.current_score += 1
        score.print_score()

    # Detect collision with wall.
    if snake.snakeBody[0].xcor() > LIMITS-10 or snake.snakeBody[0].xcor() < -LIMITS+10 or snake.snakeBody[0].ycor() < -LIMITS+10 or snake.snakeBody[0].ycor() > LIMITS-10:
        food.hideturtle()
        screen.update()
        game_is_on = False
        score.game_over()

    # Detect collision with tail.
    # If head collides with any segment in tail, game over
    for segment in snake.snakeBody[1:]:
        if snake.snakeBody[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
