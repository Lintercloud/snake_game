from turtle import *


ONE_MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segment = []
        self.start_snake()
        self.head = self.segment[0]

    #創造蛇一開始狀態
    def start_snake(self):
        for seg in range(3):
            new_snake = Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.setx(-20 * seg)
            self.segment.append(new_snake)

    #蛇吃到東西生成新蛇尾
    def extend_snake(self):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(self.segment[-1].position())
        self.segment.append(new_snake)

    #讓蛇從尾端開始先動，並讓尾端追隨下一個部尾的動作，於是我們就可以只控制蛇頭動全身
    def move(self):
            for num in range(len(self.segment) - 1, 0, -1):
                new_x = self.segment[num - 1].xcor()
                new_y = self.segment[num - 1].ycor()
                self.segment[num].goto(new_x, new_y)
            self.segment[0].forward(ONE_MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)