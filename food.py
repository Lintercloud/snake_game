from turtle import *
import random

class Food(Turtle):

    def __init__(self):
       super().__init__()
       self.shape("circle")
       self.shapesize(0.5, 0.5)
       self.color("blue")
       self.speed(0)
       self.penup()
       self.random_food()


    #讓食物隨機生成
    def random_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)