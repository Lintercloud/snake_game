from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.title("Snake game")
screen.bgcolor("black")


screen.tracer(0)

snake = Snake()

# 讓鍵盤控制蛇
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
food = Food()
score_board = Scoreboard()
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:         #檢測蛇吃到食物
        print("mom mom mom")
        food.random_food()
        score_board.get_score()
        snake.extend_snake()
        print(score_board.score)

    #檢測蛇碰到邊界
    if snake.head.xcor() > 310 or snake.head.xcor() < -310 or snake.head.ycor() > 310 or snake.head.xcor() < -310:
        is_game_on = False
        score_board.game_over()

    #檢測蛇碰到蛇尾
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 15:
            is_game_on = False
            score_board.game_over()




screen.exitonclick()


