from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()
    snake.switch_wall()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False

scoreboard.game_over()
screen.exitonclick()
